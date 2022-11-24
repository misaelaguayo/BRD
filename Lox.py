import sys
from TokenType import Token, TokenType
from Expr import Expr

"""
Lox syntactic grammar:

ambiguous grammar
---------------------------------------------------------------
epxression -> literal | unary | binary | grouping
literal -> NUMBER | STRING | 'true' | 'false' | 'nil'
grouping -> "(" expression ")"
unary -> ("-" | "!") expression
binary -> expression operator expression
operator -> "==" | "!=" | "<" | "<=" | ">" | "+" | "-" | "*" | "/"

unambiguous grammar
---------------------------------------------------------------
program -> statement* EOF ;
statement -> exprStmt | printStmt
exprStmt -> expression ";"
printStmt -> "print" expression ";"
expression -> equality
equality -> comparison(("!="|"==") comparison)*
comparison -> term((">"|">="|"<"|"<=")term)*
term -> factor(("-"|"+")factor)*
factor -> unary(("/"|"*")unary)*
unary -> ("!"|"-") unary | primary
primary -> NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")"
"""

class RunTimeError(Exception):
    def __init__(self, token: Token, message: str):
        self.token = token
        self.message = message
        super().__init__(self.message)

class Lox:
    def runtimeError(self, error: RunTimeError):
        self.hadRunTimeError = True
        print(error)

    def report(self, line: int, where: str, message: str):
        print(f"[line {line}] Error {where}: {message}")
        self.hadError = True

    def error(self, line: int = 0, message: str = "", token: Token | None = None):
        if not token:
            self.report(line, "", message)
        else:
            if token.type == TokenType.EOF:
                self.report(token.line, " at end", message)
            else:
                self.report(token.line, f" at'{token.lexeme}'", message)

    def run(self, source: str) -> None:
        from Parser import Parser
        from Scanner import Scanner
        from Interpreter import Interpreter
        tokens = Scanner(source, self).scanTokens()
        parser: Parser = Parser(tokens, self)
        expression: Expr | None = parser.parse()
        if not expression:
            return
        Interpreter().interpret(expression)

    def runPrompt(self):
        while True:
            line = input("> ")
            if not line:
                break
            self.run(line)

    def runFile(self, path: str) -> None:
        raise NotImplementedError("Has not been implemented yet!")

    def __init__(self) -> None:
        self.hadError = False

        if len(sys.argv) > 2:
            raise Exception("Usage:plox [script]")
        elif len(sys.argv) == 2:
            self.runFile(sys.argv[0])
        else:
            self.runPrompt();

Lox()
