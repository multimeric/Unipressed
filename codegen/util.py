import ast
from typing import Iterable


def make_literal(name: ast.Name, fields: Iterable[ast.Constant]) -> ast.AnnAssign:
    return ast.AnnAssign(
        target=name,
        annotation=ast.Name("TypeAlias"),
        value=ast.Subscript(
            value=ast.Name("Literal", ctx=ast.Load()), slice=ast.Tuple(elts=fields)
        ),
        simple=True,
    )
