import ast
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List

import black
import requests
import typer

app = typer.Typer(result_callback=lambda x: print(x))


def make_function(
    source_type: ast.expr, dest_type: ast.expr, taxon_id: bool, overload: bool = True
) -> ast.FunctionDef:
    """
    Makes a `submit()` function definition, as used by the ID mapper

    Params:
        source_type: Type of the `source` argument
        dest_type: Type of the `dest` argument
        taxon_id: If true, include the `taxon_id` parameter
        overload: If true, this is a function overload
    """
    args: List[ast.arg] = [
        ast.arg(
            arg="cls",
        ),
        # source: Literal[...]
        ast.arg(
            arg="source",
            annotation=source_type,
        ),
        # source: dest[...]
        ast.arg(
            arg="dest",
            annotation=dest_type,
        ),
        # ids: Iterable[str]
        ast.arg(
            "ids",
            ast.Subscript(ast.Name("Iterable"), ast.Name("str")),
        ),
    ]
    defaults: list[ast.expr | None] = [None, None, None]

    if taxon_id:
        # taxon_id: Optional[str] = None
        args.append(
            # taxon_id: bool
            ast.arg(
                "taxon_id",
                annotation=ast.Subscript(ast.Name("Optional"), ast.Name("int")),
            )
        )
        defaults.append(ast.Constant(None))

    decorator_list: list[ast.expr] = [
        ast.Name("classmethod"),
    ]
    if overload:
        decorator_list.append(
            ast.Name("overload"),
        )

    return ast.FunctionDef(
        name=f"submit",
        args=ast.arguments(
            posonlyargs=[], args=args, kwonlyargs=[], kw_defaults=[], defaults=defaults  # type: ignore
        ),
        body=[ast.Expr(ast.Constant(value=...))],
        decorator_list=decorator_list,
    )


@dataclass
class Rule:
    """
    Represents a "rule" in the Uniprot API terminology, which is a method overload
    in the Unipressed world. A rule is a set of allowed conversions from one database
    to another.
    """

    #: Rule ID
    id: int = 0
    #: List of databases that can be converted to, in this rule
    tos: list[ast.Constant] = field(default_factory=list)
    #: List of databases that can be converted from, in this rule
    froms: list[ast.Constant] = field(default_factory=list)
    #: Whether this rule supports specifying the taxon ID
    taxon_id: bool = False

    def to_function(self) -> ast.FunctionDef:
        return make_function(
            source_type=ast.Subscript(
                value=ast.Name("Literal"),
                slice=ast.Tuple(elts=self.froms),
            ),
            dest_type=ast.Subscript(
                value=ast.Name("Literal"),
                slice=ast.Tuple(elts=self.tos),  # type: ignore
            ),
            taxon_id=self.taxon_id,
            overload=True,
        )


@app.command()
def main():
    rules: defaultdict[int, Rule] = defaultdict(Rule)

    # Build up a list of rules
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

    # Create a class that has one method overload per rule
    module = ast.Module(
        body=[
            ast.ImportFrom(
                module="typing_extensions",
                names=[
                    ast.alias("Literal"),
                    ast.alias("overload"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="typing",
                names=[
                    ast.alias("Iterable"),
                    ast.alias("Optional"),
                ],
                level=0,
            ),
            ast.ClassDef(
                name="SubmitDummyClass",
                body=[
                    *[rule.to_function() for rule in rules.values()],
                    make_function(
                        source_type=ast.Name("str"),
                        dest_type=ast.Name("str"),
                        taxon_id=True,
                        overload=False,
                    ),
                ],
                decorator_list=[],
                bases=[],
                keywords=[],
            ),
        ],
        type_ignores=[],
    )

    # Produce the formatted output
    print(
        black.format_file_contents(
            ast.unparse(ast.fix_missing_locations(module)),
            fast=False,
            mode=black.FileMode(),
        )
    )


if __name__ == "__main__":
    app()
