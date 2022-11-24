from Expr import Visitor, Literal, Grouping, Expr, Unary, Binary
from TokenType import TokenType, Token
from Lox import RunTimeError, Lox

class Interpreter(Visitor):
    def __init__(self, lox: Lox):
        self.loxSingleton = lox

    @staticmethod
    def stringify(object: object) -> str:
        if not object:
            return "nil"
        if isinstance(object, float):
            text: str = str(object)
            if text[-2:] == ".0":
                text = text[0:-2]
            return text
        return str(object)
    def checkNumberOperands(self, operator: Token, left: object, right: object) -> None:
        if (isinstance(left, float) or isinstance(left, int)) and (isinstance(right, float) or isinstance(right, int)):
            return
        raise RunTimeError(operator, "Operands must be numbers")

    def checkNumberOperand(self, operator: Token, operand: object) -> None:
        if isinstance(operand, float) or isinstance(operand, int):
            return
        raise RunTimeError(operator, "Operand must be a number")

    def isTruthy(self, object: object) -> bool:
        if not object:
            return False
        if isinstance(object, bool):
            return bool(object)
        return True

    @staticmethod
    def isEqual(a: object, b: object):
        if not a and not b:
            return True
        if not a:
            return False
        return a == b

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    @staticmethod
    def visitLiteralExpr(expr: Literal) -> object:
        return expr.value

    def visitGroupingExpr(self, expr: Grouping) -> object:
        return self.evaluate(expr.expression)

    def visitUnaryExpr(self, expr: Unary) -> object:
        right: object = self.evaluate(expr.right)
        assert right is not None, "right somehow none"

        match expr.operator.type:
            case TokenType.BANG:
                return not self.isTruthy(right)
            case TokenType.MINUS:
                self.checkNumberOperand(expr.operator, right)
                return -float(right)
        return None

    def visitBinaryExpr(self, expr: Binary) -> object:
        left: object = self.evaluate(expr.left)
        right: object = self.evaluate(expr.right)

        assert left is not None and right is not None, "left or right are somehow none"

        match expr.operator.type:
            case TokenType.MINUS:
                self.checkNumberOperand(expr.operator, right)
                return float(left) - float(right)
            case TokenType.SLASH:
                self.checkNumberOperands(expr.operator, left, right)
                if not float(right):
                    raise RunTimeError(expr.operator, "Division by zero error")
                return float(left) / float(right)
            case TokenType.STAR:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) * float(right)
            case TokenType.PLUS:
                if (isinstance(left, float) or isinstance(left, int)) and (isinstance(right, float) or isinstance(right, int)):
                    return float(left) + float(right)
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                raise RunTimeError(expr.operator, "Operands must be two numbers or two strings")
            case TokenType.GREATER:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) > float(right)
            case TokenType.GREATER_EQUAL:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) >= float(right)
            case TokenType.LESS:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) < float(right)
            case TokenType.LESS_EQUAL:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) <= float(right)
            case TokenType.BANG_EQUAL:
                return not self.isEqual(left, right)
            case TokenType.EQUAL_EQUAL:
                return self.isEqual(left,right)
        return None

    def interpret(self, expression: Expr) -> None:
        try:
            value: object = self.evaluate(expression)
            print(self.stringify(value))
        except RunTimeError as e:
            self.loxSingleton.runtimeError(e)
