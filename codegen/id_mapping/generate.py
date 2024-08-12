import ast
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Sequence

import black
import requests
import typer

from codegen.util import make_literal

app = typer.Typer(result_callback=lambda x: print(x))


@dataclass
class Rule:
    id: int = 0
    tos: list[ast.Constant] = field(default_factory=list)
    froms: list[ast.Constant] = field(default_factory=list)
    taxon_id: bool = False

    def to_typed_dict(self) -> ast.ClassDef:
        body: Sequence[ast.AnnAssign] = [
            # source: Literal[...]
            ast.AnnAssign(
                ast.Name("source"),
                ast.Subscript(
                    value=ast.Name("Literal"),
                    slice=ast.Tuple(elts=self.froms),  # type: ignore
                ),
                simple=1,
            ),
            # dest: Literal[...]
            ast.AnnAssign(
                ast.Name("dest"),
                ast.Subscript(
                    value=ast.Name("Literal"),
                    slice=ast.Tuple(elts=self.tos),  # type: ignore
                ),
                simple=1,
            ),
            # ids: Iterable[str]
            ast.AnnAssign(
                ast.Name("ids"),
                ast.Subscript(ast.Name("Iterable"), ast.Name("str")),
                simple=1,
            ),
        ]

        if self.taxon_id:
            body.append(
                # taxon_id: bool
                ast.AnnAssign(
                    target=ast.Name("taxon_id"),
                    annotation=ast.Name("bool"),
                    value=None,
                    simple=1,
                )
            )

        return ast.ClassDef(
            name=f"Rule{self.id}",
            bases=[ast.Name("TypedDict")],
            body=body,  # type: ignore
            keywords=[],
            decorator_list=[],
        )


@app.command()
def main():
    rules: defaultdict[int, Rule] = defaultdict(Rule)

    type_info = requests.get(
        "https://rest.uniprot.org/configure/idmapping/fields"
    ).json()
    for group_info in type_info["groups"]:
        for item in group_info["items"]:
            if item["from"]:
                rules[item["ruleId"]].froms.append(ast.Constant(item["name"]))
    for rule_info in type_info["rules"]:
        rule = rules[rule_info["ruleId"]]
        for to in rule_info["tos"]:
            rule.tos.append(ast.Constant(to))
        rule.taxon_id = rule_info["taxonId"]
        rule.id = rule_info["ruleId"]

    module = ast.Module(
        body=[
            ast.ImportFrom(
                module="typing_extensions",
                names=[
                    ast.alias("Literal"),
                    ast.alias("TypedDict"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="typing",
                names=[
                    ast.alias("Iterable"),
                ],
                level=0,
            ),
            *[rule.to_typed_dict() for rule in rules.values()],
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
