import sys


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
primary -> equality
equality -> comparison(("!="|"==") comparison)*
comparison -> term((">"|">="|"<"|"<=")term)*
term -> factor(("-"|"+")factor)*
primary -> NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")"
unary -> ("!"|"-") unary | primary
factor -> unary(("/"|"*")unary)*
"""

class Lox:
    def run(self, source: str) -> None:
        tokens = source.split(" ")
        for token in tokens:
            print(token)

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
