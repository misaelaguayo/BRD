from Expr import *
from typing import List

class AstPrinter(Visitor):
    def print(self, expr):
        return expr.accept(self)

    def parenthesize(self, name: str, exprs: List[Expr]) -> str:
        ret = ""
        ret += f"({name}"
        for expr in exprs:
            ret += " "
            expr.accept(self)
        ret += ")"
        return ret

    def visitBinaryExpr(self, expr: Binary):
        return self.parenthesize(expr.operator.lexeme, [expr.left, expr.right])

    def visitGroupingExpr(self, expr):
        return self.parenthesize("group", [expr.expression])

    def visitLiteralExpr(self, expr: Literal):
        return "nil" if not expr.value else str(expr.value)

    def visitUnaryExpr(self, expr: Unary):
        return self.parenthesize(expr.operator.lexeme, [expr.right])

if __name__ == "__main__":
    ...
