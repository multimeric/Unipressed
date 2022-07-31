from __future__ import annotations

from typing import Any, Iterable, Optional, cast, get_args
import black
import requests
import typer
from uniprot_rest.dataset import Dataset
import ast
import humps
from pathlib import Path

# If the functions return anything, print it
app = typer.Typer(result_callback=lambda x: print(x))


def sanitize(name: str) -> str:
    # Don't need a more generalizable solution here since it's unlikely the possible
    # characters will change a great deal
    return (
        name.replace("-", "_")
        .replace("3", "three")
        .replace("2", "two")
        .replace("&", "")
        .replace("/", "")
        .replace("(", "")
        .replace(")", "")
    )



def make_literal(name: ast.Name, fields: Iterable[ast.Constant]) -> ast.AnnAssign:
    return ast.AnnAssign(
        target=name,
        annotation=ast.Name("TypeAlias"),
        value=ast.Subscript(
            value=ast.Name("Literal", ctx=ast.Load()), slice=ast.Tuple(elts=fields)
        ),
        simple=True,
    )


def make_query_dict(name: str, fields: Iterable[ast.AnnAssign]) -> ast.AnnAssign:
    """Makes a TypedDict that defines the structure of some dictionary used in the query tree

    Args:
        name (str): The name of the type
        fields (Iterable[ast.AnnAssign]): A list of fields for this dictionary

    Raises:
        Exception: If any of the fields are complex assignments such as tuple unpacking

    Returns:
        tuple[ast.ClassDef, ast.Dict]: The first element is the newly generated TypedDict, and the second a Dict containing new entries to the lookup table
    """
    # Add the baseline conjunctions
    mapping = ast.Dict(keys=[ast.Constant("and"), ast.Constant("or")], values=[ast.Name(f"Iterable[{name}]")] * 2)

    # Add the fields for this dataset
    for field in fields:
        if not isinstance(field.target, ast.Name):
            raise Exception("")

        mapping.keys.append(ast.Constant(field.target.id))
        mapping.values.append(field.annotation)

    return ast.AnnAssign(
        target=ast.Name(name),
        annotation=ast.Name("TypeAlias"),
        value=ast.Call(func=ast.Name("TypedDict"), args=[ast.Constant(name), mapping], keywords=[]),
        simple=True
    )


def convert_type(
    field: dict[str, Any], enclose: Optional[str] = None
) -> tuple[ast.expr, Iterable[ast.stmt]]:
    """Returns the annotation type, and then a collection of stuff to add to the module
    body to support it (ie class definitions).

    Args:
        field: Uniprot field description, as obtained from the API
        enclose: An optional type to wrap around the generated type annotation, e.g. Optional or NotRequired
    """
    ret: tuple[ast.Name, Iterable[ast.stmt]]
    if field["fieldType"] == "general":
        if field["dataType"] == "string":
            ret = ast.Name("str"), []
        elif field["dataType"] == "enum":
            name = field["id"].capitalize()
            ret = ast.Name(f"{name}"), [
                make_literal(
                    name=ast.Name(name),
                    fields=[ast.Constant(it["value"]) for it in field["values"]],
                )
            ]
        elif field["dataType"] == "integer":
            ret = ast.Name("int"), []
        elif field["dataType"] == "date":
            ret = ast.Name("date"), []
        elif field["dataType"] == "boolean":
            ret = ast.Name("bool"), []
        else:
            raise Exception()
    elif field["fieldType"] == "evidence" and field["dataType"] == "string":
        name = humps.camelize(field["id"])
        evidence_literal = make_literal(
            name=ast.Name(name + "Evidence"),
            fields=[
                ast.Constant(item["code"]) for group in field["evidenceGroups"] for item in group["items"]
            ]
        )
        evidence_docstring = "\n".join([
                f"{item['code']}: {item['name']}" for group in field["evidenceGroups"] for item in group["items"]
            ])

        ret = ast.Name(name), [
            evidence_literal,
            ast.ClassDef(
            name = name,
            bases = [ast.Name("TypedDict")],
            keywords = [],
            decorator_list = [],
            body = [
                ast.AnnAssign(
                    target = ast.Name("query"),
                    annotation = ast.Name("str"),
                    simple=True
                ),
                ast.AnnAssign(
                    target = ast.Name("evidence"),
                    annotation = evidence_literal.target,
                    simple=True
                ),
                ast.Expr(ast.Constant(evidence_docstring))
            ]
        )
        ]
    elif field["fieldType"] == "range":
        if field["dataType"] == "integer":
            ret = ast.Subscript(
                value = ast.Name("tuple"),
                slice = ast.Tuple(
                    elts = [
                        ast.Name("int"),
                        ast.Name("int")
                    ]
                )
            ), []
        elif field["dataType"] == "date":
            ret = ast.Subscript(
                value = ast.Name("tuple"),
                slice = ast.Tuple(
                    elts = [
                        ast.Name("date"),
                        ast.Name("date")
                    ]
                )
            ), []
        else:
            raise Exception()
    else:
        raise Exception()


    if enclose is not None:
        return ast.Subscript(
            value = ast.Name(enclose),
            slice = ret[0]
        ), ret[1]

    return ret


def iter_subfields(field: dict[str, Any]) -> Iterable[dict[str, Any]]:
    """
    Returns a generator that recursively generates all fields within groups and subgroups
    """
    if field["itemType"] == "group":
        for subfield in field["items"]:
            yield from iter_subfields(subfield)
    elif field["itemType"] == "sibling_group":
        for subfield in field["siblings"]:
            yield from iter_subfields(subfield)
    else:
        yield field


def generate_return_fields(dataset: Dataset, type_name: str) -> Iterable[ast.stmt]:
    """
    Generates the code describing the "fields" aka the configurable return values for
    this dataset
    :param dataset: The dataset enum instance defining the dataset to generate code for
    :param type_name: The name of the top level type (which is a TypedDict)
    :return: A tuple of (top level statements, exports as string constants)
    """
    top_level: list[ast.stmt] = []
    groups = ast.Tuple(elts=[])

    for group in requests.get(
        f"https://rest.uniprot.org/configure/{dataset}/result-fields"
    ).json():
        group_name: str = humps.pascalize(
            sanitize(dataset.capitalize() + "_" + group["id"])
        )
        # Create a new Literal for all fields in this group
        top_level.append(
            make_literal(
                ast.Name(group_name),
                [ast.Constant(it["name"]) for it in group["fields"]],
            )
        )
        # Keep track of all the groups so we can union them together
        groups.elts.append(ast.Name(group_name))

    # Make a type union over all the Literals which is user facing
    top_level.append(
        ast.AnnAssign(
            target=ast.Name(type_name),
            annotation=ast.Name("TypeAlias"),
            value=ast.Subscript(value=ast.Name("Literal"), slice=groups),
            simple=True,
        )
    )

    return top_level


def generate_query_fields(dataset: Dataset, type_name: str) -> Iterable[ast.stmt]:
    """
    Generates the code describing the query types for this dataset
    :param: dataset The dataset enum instance defining the dataset to generate code for
    :param type_name: The name of the top level type (which is a TypedDict)
    :return: A tuple of (top level statements, exports as string constants)
    """
    top_level: list[ast.stmt] = []
    fields: list[ast.AnnAssign] = []

    # Iterate over all query fields
    response = requests.get(
        f"https://rest.uniprot.org/configure/{dataset}/search-fields"
    )
    response.raise_for_status()
    for field in response.json():
        for subfield in iter_subfields(field):
            typ, extra = convert_type(subfield, enclose="NotRequired")
            top_level += extra

            # For each field, annotate the top level query TypedDict
            fields.append(
                ast.AnnAssign(
                    target=ast.Name(subfield["id"]), annotation=typ, simple=True
                )
            )

    # Create the top level TypedDict
    top_level.append(make_query_dict(name=type_name, fields=fields))

    return top_level


def generate_search_subclass(
    dataset: Dataset, query_type: ast.Name, field_type: ast.Name
) -> ast.ClassDef:
    """Makes the definition of a dataset-specific Search class such as UnirefSearch

    Args:
        dataset (Dataset): The dataset for which to generate the class
        query_type (ast.Name): The name of the type the defines valid queries to this database
        field_type (ast.Name): The name of the type that defines valid fields for this database
    """
    return ast.ClassDef(
        name=dataset.capitalize() + "Search",
        bases=[ast.Name("uniprot_rest.Search")],
        body=[
            ast.AnnAssign(
                target=ast.Name("dataset"),
                annotation=ast.Name(f'Literal["{dataset}"]'),
                simple=True,
                value=ast.Name(f'field(default="{dataset}", init=False)'),
            ),
            ast.AnnAssign(target=ast.Name("query"), annotation=query_type, simple=True),
            ast.AnnAssign(
                target=ast.Name("fields"), annotation=field_type, simple=True
            ),
        ],
        keywords=[],
        starargs=[],
        decorator_list=[ast.Name(id="dataclass")],
    )


@app.command()
def make_dataset(dataset: str):
    dataset = cast(Dataset, dataset)
    module = ast.Module(
        body=[
            ast.ImportFrom(
                module="typing",
                names=[
                    ast.alias("Union"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="typing_extensions",
                names=[
                    ast.alias("TypeAlias"),
                    ast.alias("Literal"),
                    ast.alias("TypedDict"),
                    ast.alias("NotRequired"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="dataclasses",
                names=[
                    ast.alias("dataclass"),
                    ast.alias("field"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="datetime",
                names=[
                    ast.alias("date"),
                ],
                level=0,
            ),
            ast.Import(names=[ast.alias("uniprot_rest")]),
        ],
        type_ignores=[],
    )

    dataset_name = dataset.capitalize()

    query_type_name = dataset_name + "Query"
    new_top_level = generate_query_fields(dataset, query_type_name)
    module.body += new_top_level

    field_type_name = dataset_name + "Fields"
    new_top_level = generate_return_fields(dataset, field_type_name)
    module.body += new_top_level

    module.body.append(
        generate_search_subclass(
            dataset=dataset,
            query_type=ast.Name(query_type_name),
            field_type=ast.Name(field_type_name),
        )
    )

    return black.format_file_contents(
        ast.unparse(ast.fix_missing_locations(module)),
        fast=False,
        mode=black.FileMode(),
    )


@app.command()
def make_all_datasets(root: Path):
    for dataset in get_args(Dataset):
        result = make_dataset(dataset)
        (root / f"{dataset}.py").write_text(result)


if __name__ == "__main__":
    app()
