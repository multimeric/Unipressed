from __future__ import annotations

from typing import Iterable

import requests
import typer
from uniprot_rest.types.dataset import Dataset
import ast
import humps
from pathlib import Path

app = typer.Typer(result_callback=lambda x: print(x))


def sanitize(name: str) -> str:
    # Don't need a more generalizable solution here since it's unlikely the possible
    # characters will change a great deal
    return name.replace("-", "_").replace("3", "three").replace("2", "two").replace("&", "").replace("/", "").replace("(", "").replace(")", "")


def make_enum(name: str, fields: Iterable[ast.Name]) -> ast.ClassDef:
    return ast.ClassDef(
        name=name,
        bases=[ast.Name("Enum", ast.Load)],
        keywords=[],
        starargs=[],
        decorator_list=[],
        body=[
            ast.Assign(target=it, value=ast.Call(name=ast.Name("auto")))
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
        simple=True
    )


def make_typed_dict(name: str, fields: Iterable[ast.AnnAssign]) -> ast.ClassDef:
    return ast.ClassDef(
        name=name,
        bases=[ast.Name("TypedDict", ast.Load)],
        body=fields,
        keywords=[],
        starargs=[],
        decorator_list=[],
    )


def make_dataclass(name: str, fields: Iterable[ast.AnnAssign]) -> ast.ClassDef:
    mapping = ast.Dict(
        keys=[],
        values=[]
    )

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
        new_fields.append(ast.AnnAssign(
            target=ast.Name("field_map"),
            annotation=ast.Name("ClassVar[dict]"),
            value=mapping,
            simple=True
        ))

    return ast.ClassDef(
        name=name,
        bases=[ast.Name("UniprotMixin", ast.Load)],
        body=new_fields,
        keywords=[],
        starargs=[],
        decorator_list=[ast.Name(
            id="dataclass"
        )],
    )


def convert_type(field: dict) -> tuple[ast.Name, Iterable[ast.AST]]:
    """
    Returns the annotation type, and then a collection of stuff to add to the module
    body to support it (ie class definitions)
    """
    if field["dataType"] == "string":
        return ast.Name("Optional[str]"), []
    elif field["dataType"] == "enum":
        name = field['id'].capitalize()
        return ast.Name(f"Optional[{name}]"), [
            make_literal(
                name=ast.Name(name), fields=[ast.Constant(it["value"]) for it in field["values"]]
            )
        ]
    elif field["dataType"] == "integer":
        return ast.Name("Optional[int]"), []
    elif field["dataType"] == "date":
        return ast.Name("Optional[date]"), []
    elif field["dataType"] == "boolean":
        return ast.Name("Optional[bool]"), []
    else:
        raise Exception()


def iter_subfields(field: dict) -> Iterable[dict]:
    if field["itemType"] == "group":
        for subfield in field["items"]:
            yield from iter_subfields(subfield)
    elif field["itemType"] == "sibling_group":
        for subfield in field["siblings"]:
            yield from iter_subfields(subfield)
    else:
        yield field


@app.command()
def query_fields():
    generated = ast.Module(
        body=[
            ast.ImportFrom(
                module="typing",
                names=[
                    ast.alias("ClassVar"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="typing_extensions",
                names=[
                    ast.alias("TypeAlias"),
                    ast.alias("Literal"),
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
            ast.ImportFrom(
                module="uniprot_rest.types.util",
                names=[
                    ast.alias("UniprotMixin"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="dataclasses",
                names=[
                    ast.alias("dataclass"),
                ],
                level=0,
            ),
        ],
        type_ignores=[],
    )
    exports: list[ast.Constant] = []
    for dataset in Dataset:
        fields: list[ast.AnnAssign] = []
        for field in requests.get(
                f"https://rest.uniprot.org/configure/{dataset.name}/search-fields"
        ).json():
            for subfield in iter_subfields(field):
                typ, extra = convert_type(subfield)
                generated.body += extra
                fields.append(
                    ast.AnnAssign(
                        target=ast.Name(subfield["id"]), annotation=typ, simple=True
                    )
                )
        dataset_class_name = dataset.name.capitalize()
        generated.body.append(
            make_dataclass(name=dataset_class_name, fields=fields)
        )
        exports.append(ast.Constant(dataset_class_name))

    # All the __all__ export
    generated.body.append(
        ast.Assign(
            targets=[ast.Name("__all__")],
            value=ast.List(elts=exports)
        )
    )
    print(ast.unparse(ast.fix_missing_locations(generated)))


def generate_return_fields(dataset: Dataset) -> tuple[
    Iterable[ast.AST],
    Iterable[ast.Constant],
]:
    """
    :return: A tuple of (top level statements, exports as string constants)
    """
    top_level = []
    exports = []
    groups = ast.Tuple(elts=[])

    for group in requests.get(
            f"https://rest.uniprot.org/configure/{dataset.value}/result-fields"
    ).json():
        group_name = humps.pascalize( sanitize(dataset.name.capitalize() + group["groupName"]))
        # Create a new Literal for all fields in this group
        top_level.append(make_literal(ast.Name(group_name), [ast.Constant(it["name"]) for it in group["fields"]]))
        # Keep track of all the groups so we can union them together
        groups.elts.append(ast.Name(group_name))

    # Make a type union over all the Literals which is user facing
    group_union_name = f"{dataset.name.capitalize()}Fields"
    top_level.append(ast.AnnAssign(
        target=ast.Name(group_union_name),
        annotation=ast.Name("TypeAlias"),
        value=ast.Subscript(
            value=ast.Name("Union"),
            slice=groups
        ),
        simple=True
    ))

    # Export this high-level Union
    exports.append(ast.Constant(group_union_name))

    return top_level, exports

def generate_query_fields(dataset: Dataset) -> tuple[
    Iterable[ast.AST],
    Iterable[ast.Constant]
]:
    """
    :return: A tuple of (top level statements, exports as string constants)
    """
    top_level = []
    exports: list[ast.Constant] = []
    fields: list[ast.AnnAssign] = []

    # Iterate over all query fields
    response = requests.get( f"https://rest.uniprot.org/configure/{dataset.value}/search-fields" )
    response.raise_for_status()
    for field in response.json():
        for subfield in iter_subfields(field):
            typ, extra = convert_type(subfield)
            top_level += extra

            # For each field, annotate the top level query TypedDict
            fields.append(
                ast.AnnAssign(
                    target=ast.Name(subfield["id"]), annotation=typ, simple=True
                )
            )

    # Create the top level TypedDict
    dataset_class_name = dataset.name.capitalize() + "Query"
    top_level.append(
        make_typed_dict(name=dataset_class_name, fields=fields)
    )
    # Export this
    exports.append(ast.Constant(dataset_class_name))

    return top_level, exports

@app.command()
def make_dataset(dataset: Dataset):
    module = ast.Module(body=[
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
            ],
            level=0,
        ),
        ast.ImportFrom(
            module="dataclasses",
            names=[
                ast.alias("dataclass"),
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
        ast.ImportFrom(
            module="uniprot_rest.types.util",
            names=[
                ast.alias("UniprotMixin"),
            ],
            level=0,
        ),
    ], type_ignores=[])
    exports = []

    for func in (generate_query_fields, generate_return_fields):
        new_top_level, new_exports = func(dataset)
        exports += new_exports
        module.body += new_top_level

    # All the __all__ export
    module.body.append(
        ast.Assign(
            targets=[ast.Name("__all__")],
            value=ast.List(elts=exports)
        )
    )
    return ast.unparse(ast.fix_missing_locations(module))

@app.command()
def make_all_datasets(root: Path):
    for dataset in Dataset:
        result = make_dataset(dataset)
        (root / f"{dataset.value}.py").write_text(result)

if __name__ == "__main__":
    app()
