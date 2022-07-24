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


def make_enum(name: str, fields: Iterable[ast.Name]) -> ast.ClassDef:
    return ast.ClassDef(
        name=name,
        bases=[ast.Name("Enum", ast.Load)],
        keywords=[],
        starargs=[],
        decorator_list=[],
        body=[
            ast.Assign(targets=[it], value=ast.Call(name=ast.Name("auto")))
            for it in fields
        ],
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


def make_query_dict(name: str, fields: Iterable[ast.AnnAssign]) -> tuple[ast.ClassDef, ast.Dict]:
    """Makes a TypedDict that defines the structure of some dictionary used in the query tree

    Args:
        name (str): The name of the type
        fields (Iterable[ast.AnnAssign]): A list of fields for this dictionary 

    Raises:
        Exception: If any of the fields are complex assignments such as tuple unpacking

    Returns:
        tuple[ast.ClassDef, ast.Dict]: The first element is the newly generated TypedDict, and the second a Dict containing new entries to the lookup table
    """
    lookup = ast.Dict(
        keys = [],
        values = []
    )
    cls = ast.ClassDef(
        name=name,
        bases=[ast.Name("TypedDict", ast.Load)],
        body=[],
        keywords=[],
        starargs=[],
        decorator_list=[],
    )

    for field in fields:
        if not isinstance(field.target, ast.Name):
            raise Exception("")

        sanitized = sanitize(field.target.id)
        if sanitized != field.target.id:
            # If the sanitization process changed the key, we need to save the new and old keys in a lookup table
            lookup.keys.append(ast.Constant(sanitized))
            lookup.values.append(ast.Constant(field.target.id))
            field.target.id = sanitized

        cls.body.append(field)

    return cls, lookup


def make_typed_dict(name: str, fields: Iterable[ast.AnnAssign]) -> ast.ClassDef:
    return ast.ClassDef(
        name=name,
        bases=[ast.Name("TypedDict", ast.Load)],
        body=fields,
        keywords=[],
        starargs=[],
        decorator_list=[],
    )


def make_dataclass(
    name: str, fields: Iterable[ast.AnnAssign], base: str = None
) -> ast.ClassDef:
    mapping = ast.Dict(keys=[], values=[])

    new_fields: list[ast.AnnAssign] = []

    # Sanitize each field, to ensure that they're valid Python names, then
    # save a lookup table that allows us to find the original names
    for field in fields:
        if isinstance(field.target, ast.Name):
            field_name = field.target.id
        else:
            raise Exception()

        sanitized = sanitize(field_name)
        if field_name != sanitized:
            mapping.keys.append(ast.Constant(sanitized))
            mapping.values.append(ast.Constant(field_name))
            field.target.id = sanitized
        new_fields.append(field)

    # Add the lookup
    if len(mapping.keys) > 0:
        new_fields.append(
            ast.AnnAssign(
                target=ast.Name("field_map"),
                annotation=ast.Name("ClassVar[dict]"),
                value=mapping,
                simple=True,
            )
        )

    return ast.ClassDef(
        name=name,
        bases=[ast.Name(base, ast.Load)] if base else [],
        body=new_fields,
        keywords=[],
        starargs=[],
        decorator_list=[ast.Name(id="dataclass")],
    )


def convert_type(
    field: dict[str, Any], enclose: Optional[str] = None
) -> tuple[ast.Name, Iterable[ast.stmt]]:
    """Returns the annotation type, and then a collection of stuff to add to the module
    body to support it (ie class definitions).

    Args:
        field: Uniprot field description, as obtained from the API
        enclose: An optional type to wrap around the generated type annotation, e.g. Optional or NotRequired
    """
    ret: tuple[ast.Name, Iterable[ast.stmt]]
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

    if enclose is not None:
        ret[0].id = f"{enclose}[{ret[0].id}]"

    return ret


def iter_subfields(field: dict[str, Any]) -> Iterable[dict[str, Any]]:
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
            sanitize(dataset.capitalize() + group["groupName"])
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
            value=ast.Subscript(value=ast.Name("Union"), slice=groups),
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
    query_type, lookup = make_query_dict(name=type_name, fields=fields)
    top_level.append(query_type)
    top_level.append(ast.Assign(
        targets = [ast.Name("lookup")],
        value = lookup
    ))

    return top_level


def generate_search_subclass(
    dataset: Dataset, query_type: ast.Name, field_type: ast.Name
) -> ast.ClassDef:
    return make_dataclass(
        name=dataset.capitalize() + "Seach",
        base="uniprot_rest.Search",
        fields=[
            ast.AnnAssign(
                target=ast.Name("dataset"),
                annotation=ast.Name(f'Literal["{dataset}"]'),
                simple=True,
                value=ast.Name('field(default="uniref", init=False)'),
            ),
            ast.AnnAssign(
                target=ast.Name("query"), annotation=query_type, simple=True
            ),
            ast.AnnAssign(
                target=ast.Name("fields"), annotation=field_type, simple=True
            ),
        ],
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
                    ast.alias("Optional"),
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
            # ast.ImportFrom(
            #     module="uniprot_rest.types.util",
            #     names=[
            #         ast.alias("UniprotMixin"),
            #     ],
            #     level=0,
            # ),
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

    # # All the __all__ export
    # module.body.append(
    #     ast.Assign(
    #         targets=[ast.Name("__all__")],
    #         value=ast.List(elts=exports)
    #     )
    # )
    return black.format_file_contents(ast.unparse(ast.fix_missing_locations(module)), fast=False, mode=black.FileMode())


@app.command()
def make_all_datasets(root: Path):
    for dataset in get_args(Dataset):
        result = make_dataset(dataset)
        (root / f"{dataset.value}.py").write_text(result)


if __name__ == "__main__":
    app()
