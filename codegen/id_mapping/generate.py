import ast

import black
import requests
import typer

from codegen.util import make_literal

app = typer.Typer(result_callback=lambda x: print(x))


@app.command()
def main():
    froms: list[ast.Constant] = []
    tos: list[ast.Constant] = []

    for group in requests.get(
        "https://rest.uniprot.org/configure/idmapping/fields"
    ).json()["groups"]:
        for item in group["items"]:
            if item["from"]:
                froms.append(ast.Constant(item["name"]))
            if item["to"]:
                tos.append(ast.Constant(item["name"]))

    module = ast.Module(
        body=[
            ast.ImportFrom(
                module="typing_extensions",
                names=[
                    ast.alias("Literal"),
                    ast.alias("TypeAlias"),
                ],
                level=0,
            ),
            make_literal(ast.Name("From"), froms),
            make_literal(ast.Name("To"), tos),
        ],
        type_ignores=[],
    )

    print(
        black.format_file_contents(
            ast.unparse(ast.fix_missing_locations(module)),
            fast=False,
            mode=black.FileMode(),
        )
    )


if __name__ == "__main__":
    app()
