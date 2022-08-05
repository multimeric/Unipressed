from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional, cast, get_args

import black
import inflection
import requests
import typer
from uniprot_types import UniprotSearchField

from unipressed.dataset import Dataset

# If the functions return anything, print it
app = typer.Typer(result_callback=lambda x: print(x))


def make_description(field: UniprotSearchField) -> str:
    """
    Generate a docstring for a field
    """
    ret = [field.get("label", make_placeholder_description(field["term"]))]
    if "example" in field:
        ret.append(f"e.g. {field['example']}")
    # We try to document all the enum options within the TypedDict, since Literals don't support docstrings
    for value in field.get("values", []):
        ret.append(f"* {value['value']}: {value['name']}")
    return "\n".join(ret)


def make_placeholder_description(field_name: str) -> str:
    """
    Generates a sentence from a field name, where no description was provided
    """

    def _gen():
        for i, field in enumerate(field_name.split("_")):
            if field == field.upper():
                yield field
            elif i == 0:
                yield field.capitalize()
            else:
                yield field.lower()

    return " ".join(_gen())
    # return inflection.titleize(field_name).replace("id", "ID")


@dataclass
class FieldDefinition:
    name: str
    description: Optional[str]
    type: ast.expr

    def to_ann_assign(self) -> ast.AnnAssign:
        return ast.AnnAssign(
            target=ast.Name(self.name), annotation=self.type, simple=True
        )

    def to_dict(self) -> tuple[ast.expr, ast.expr]:
        return ast.Constant(self.name), self.type


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
        .replace("__", "_")
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


def make_query_dict(name: str, fields: Iterable[FieldDefinition]) -> ast.ClassDef:
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
    body: list[ast.stmt] = [
        ast.AnnAssign(
            ast.Name("and_"),
            annotation=ast.Subscript(
                ast.Name("NotRequired"),
                ast.Subscript(ast.Name("Iterable"), ast.Constant(name)),
            ),
            simple=True,
        ),
        ast.Expr(ast.Constant("Two or more filters that must both be satisfied")),
        ast.AnnAssign(
            ast.Name("or_"),
            annotation=ast.Subscript(
                ast.Name("NotRequired"),
                ast.Subscript(ast.Name("Iterable"), ast.Constant(name)),
            ),
            simple=True,
        ),
        ast.Expr(ast.Constant("Two or more filters, any of which can be satisfied")),
        ast.AnnAssign(
            ast.Name("not_"),
            annotation=ast.Subscript(
                ast.Name("NotRequired"),
                ast.Subscript(ast.Name("Iterable"), ast.Constant(name)),
            ),
            simple=True,
        ),
        ast.Expr(ast.Constant("Negate a filter")),
    ]
    mapping = ast.Dict(keys=[], values=[])

    # We have to sort the fields into those that can be class variables and those that have to be defined as strings (because they aren't valid identifiers)
    for field in fields:
        if field.name.isidentifier():
            body.append(field.to_ann_assign())
            # Add the docstring
            if field.description:
                body.append(ast.Expr(ast.Constant(field.description)))
        else:
            key, value = field.to_dict()
            mapping.keys.append(key)
            mapping.values.append(value)

    return ast.ClassDef(
        name=name,
        bases=[
            ast.Call(
                ast.Name("TypedDict"), args=[ast.Constant(name), mapping], keywords=[]
            )
            if len(mapping.keys) > 0
            else ast.Name("TypedDict")
        ],
        body=body,
        decorator_list=[],
        keywords=[],
    )


def convert_type(
    field: UniprotSearchField, enclose: Optional[str] = None
) -> tuple[Iterable[FieldDefinition], Iterable[ast.stmt]]:
    """Returns the annotation type, and then a collection of stuff to add to the module
    body to support it (ie class definitions).

    Args:
        field: Uniprot field description, as obtained from the API
        enclose: An optional type to wrap around the generated type annotation, e.g. Optional or NotRequired
    """
    fields: list[FieldDefinition] = []
    extra: list[ast.stmt] = []
    description: str = make_description(field)

    def add_entry(rhs: ast.expr):
        fields.append(
            FieldDefinition(name=field["term"], type=rhs, description=description)
        )

    # ret: tuple[Iterable[ast.AnnAssign], Iterable[ast.stmt]]
    if field["fieldType"] == "general":
        if field["dataType"] == "string":
            add_entry(ast.Name("str"))
        elif field["dataType"] == "enum":
            name = inflection.camelize(field["id"], True)
            fields.append(
                FieldDefinition(
                    name=field["term"],
                    type=ast.Name(f"{name}"),
                    description=description,
                )
            )
            extra.append(
                make_literal(
                    name=ast.Name(name),
                    fields=[ast.Constant(it["value"]) for it in field["values"]],
                )
            )
        elif field["dataType"] == "integer":
            add_entry(ast.Name("int"))
        elif field["dataType"] == "date":
            add_entry(ast.Name("date"))
        elif field["dataType"] == "boolean":
            add_entry(ast.Name("bool"))
        else:
            raise Exception()
    elif field["fieldType"] == "evidence" and field["dataType"] == "string":
        # For some reason, the go field has implicit subfields, but none of the other evidence fields does this
        if field["id"].endswith("evidence"):
            for group in field["evidenceGroups"]:
                for item in group["items"]:
                    if item["code"] != "any":
                        fields.append(
                            FieldDefinition(
                                name=f"{field['term']}_{item['code']}",
                                type=ast.Name("str"),
                                description=f'{field["term"]}, {item["name"].lower()}',
                            )
                        )
        else:
            add_entry(ast.Name("str"))

    elif field["fieldType"] == "range":
        if field["dataType"] == "integer":
            add_entry(
                ast.Subscript(
                    value=ast.Name("tuple"),
                    slice=ast.Tuple(
                        [
                            ast.Subscript(
                                ast.Name("Union"),
                                slice=ast.Tuple(
                                    [
                                        ast.Name("int"),
                                        ast.Subscript(
                                            ast.Name("Literal"),
                                            slice=ast.Tuple([ast.Constant("*")]),
                                        ),
                                    ]
                                ),
                            )
                        ]
                        * 2
                    ),
                )
            )
        elif field["dataType"] == "date":
            add_entry(
                ast.Subscript(
                    value=ast.Name("tuple"),
                    slice=ast.Tuple(
                        [
                            ast.Subscript(
                                ast.Name("Union"),
                                slice=ast.Tuple(
                                    [
                                        ast.Name("date"),
                                        ast.Subscript(
                                            ast.Name("Literal"),
                                            slice=ast.Tuple([ast.Constant("*")]),
                                        ),
                                    ]
                                ),
                            )
                        ]
                        * 2
                    ),
                )
            )
        else:
            raise Exception()
    else:
        raise Exception()

    autocomplete = field.get("autoCompleteQueryTerm")
    if autocomplete is not None and autocomplete != field["term"]:
        fields.append(
            FieldDefinition(
                # We don't have a propert description for autocomplete fields
                name=autocomplete,
                type=ast.Name("str"),
                description=make_placeholder_description(autocomplete),
            )
        )

    # Add the e.g. NotRequired annotation
    if enclose is not None:
        for field_def in fields:
            field_def.type = ast.Subscript(
                value=ast.Name(enclose), slice=field_def.type
            )

    return fields, extra


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
        group_name: str = inflection.camelize(
            sanitize(dataset.capitalize() + "_" + group["id"]),
            uppercase_first_letter=True,
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
    fields: list[FieldDefinition] = []
    # We use a set here to deduplicate fields with the same name
    field_names: set[str] = set()

    # Iterate over all query fields
    response = requests.get(
        f"https://rest.uniprot.org/configure/{dataset}/search-fields"
    )
    response.raise_for_status()
    for field in response.json():
        for subfield in iter_subfields(field):
            new_fields, extra = convert_type(subfield, enclose="NotRequired")
            top_level += extra

            for field in new_fields:
                # If we see an assignment expression, skip it if we've seen that field name before
                if field.name in field_names:
                    continue
                else:
                    fields.append(field)
                    field_names.add(field.name)

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
        bases=[ast.Name("unipressed.base.Search")],
        body=[
            ast.Expr(
                ast.Constant(
                    f"Client for querying the [{dataset} Uniprot dataset](https://www.uniprot.org/help/{dataset})"
                )
            ),
            ast.AnnAssign(
                target=ast.Name("dataset"),
                annotation=ast.Name(f'Literal["{dataset}"]'),
                simple=True,
                value=ast.Name(f'field(default="{dataset}", init=False)'),
            ),
            ast.AnnAssign(target=ast.Name("query"), annotation=query_type, simple=True),
            ast.Expr(ast.Constant("A query that filters the returned proteins")),
            ast.AnnAssign(
                target=ast.Name("fields"),
                annotation=ast.Subscript(ast.Name("Iterable"), field_type),
                simple=True,
            ),
            ast.Expr(ast.Constant("Fields to return in the result object")),
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
                module="__future__",
                names=[
                    ast.alias("annotations"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="typing",
                names=[
                    ast.alias("Union"),
                    ast.alias("Iterable"),
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
            ast.Import(names=[ast.alias("unipressed.base")]),
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
