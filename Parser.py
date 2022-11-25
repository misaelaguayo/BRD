from typing import List
from TokenType import Token, TokenType
from Expr import Expr, Binary, Unary, Literal, Grouping, Variable, Assign
from Stmt import Stmt, Print, Expression, Var
from Lox import Lox

class ParseError(Exception):
    def __init__(self, token: Token, message: str, lox: Lox):
        self.token = token
        self.message = message
        lox.error(token=token, message=message)

class Parser:
    def __init__(self, tokens: List[Token], lox: Lox):
        self.tokens: List[Token] = tokens
        self.current: int = 0
        self.loxSingleton = lox

    def expressionStatement(self) -> Stmt:
        expr: Expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after expression.")
        return Expression(expr)

    def printStatement(self) -> Stmt:
        value: Expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after value.")
        return Print(value)

    def statement(self) -> Stmt:
        if self.match([TokenType.PRINT]):
            return self.printStatement()
        return self.expressionStatement()

    def varDeclaration(self) -> Stmt | None:
        name: Token = self.consume(TokenType.IDENTIFIER, "Expect variable name.")
        initializer = None

        if self.match([TokenType.EQUAL]):
            initializer = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after variable declaration.")
        if initializer:
            return Var(name, initializer)
        return None


    def declaration(self) -> Stmt | None:
        try:
            if self.match([TokenType.VAR]):
                return self.varDeclaration()
            return self.statement()
        except ParseError:
            self.synchronize()
            return None

    def parse(self) -> List[Stmt]:
        statements: List[Stmt] = []
        while not self.isAtEnd():
            dec = self.declaration()
            if dec:
                statements.append(dec)
        return statements

    def synchronize(self) -> None:
        self.advance()
        while not self.isAtEnd():
            if self.previous().type == TokenType.SEMICOLON:
                return
            match self.peek().type:
                case TokenType.CLASS | TokenType.FOR | TokenType.FUN | TokenType.IF | TokenType.PRINT | TokenType.RETURN | TokenType.VAR | TokenType.WHILE:
                    return
            self.advance()
    def consume(self, type: TokenType, message: str):
        if self.check(type):
            return self.advance()
        raise ParseError(self.peek(), message, self.loxSingleton)

    def primary(self) -> Expr:
        if self.match([TokenType.FALSE]):
            return Literal(TokenType.FALSE)
        if self.match([TokenType.TRUE]):
            return Literal(TokenType.TRUE)
        if self.match([TokenType.NIL]):
            return Literal(None)
        if self.match([TokenType.NUMBER, TokenType.STRING]):
            return Literal(self.previous().literal)
        if self.match([TokenType.IDENTIFIER]):
            return Variable(self.previous())
        if self.match([TokenType.LEFT_PAREN]):
            expr: Expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)
        else:
            raise ParseError(self.peek(), "Expect expression.", self.loxSingleton)

    def unary(self) -> Expr:
        if self.match([TokenType.BANG, TokenType.MINUS]):
            operator: Token = self.previous()
            right: Expr = self.unary()
            return Unary(operator, right)
        return self.primary()

    def factor(self) -> Expr:
        expr: Expr = self.unary()

        while self.match([TokenType.SLASH, TokenType.STAR]):
            operator: Token = self.previous()
            right: Expr = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def term(self) -> Expr:
        expr: Expr = self.factor()
        while self.match([TokenType.MINUS, TokenType.PLUS]):
            operator: Token = self.previous()
            right: Expr = self.factor()
            expr = Binary(expr, operator, right)
        return expr

    def comparison(self) -> Expr:
        expr: Expr = self.term()
        while self.match([TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL]):
            operator: Token = self.previous()
            right: Expr = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def previous(self):
        return self.tokens[self.current - 1]

    def peek(self) -> Token:
        return self.tokens[self.current]

    def isAtEnd(self):
        return self.peek().type == TokenType.EOF

    def advance(self) -> Token:
        if not self.isAtEnd():
            self.current += 1
        return self.previous()

    def check(self, type: TokenType) -> bool:
        if self.isAtEnd():
            return False
        return self.peek().type == type

    def match(self, types: List[TokenType]) -> bool:
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def equality(self) -> Expr:
        expr: Expr = self.comparison()
        while self.match([TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL]):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def assignment(self) -> Expr:
        expr: Expr = self.equality()
        if self.match([TokenType.EQUAL]):
            equals: Token = self.previous()
            value: Expr = self.assignment()
            if isinstance(expr, Variable):
                name: Token = expr.name
                return Assign(name, value)
            self.loxSingleton.error(token=equals, message="Invalid assignment target.")
        return expr

    def expression(self) -> Expr:
        return self.assignment()
