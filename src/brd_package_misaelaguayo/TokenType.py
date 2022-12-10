from enum import Enum, auto
from typing import Any


class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    COMMA = ","
    DOT = "."
    MINUS = "-"
    PLUS = "+"
    SEMICOLON = ";"
    SLASH = "/"
    STAR = "*"

    # One or two character tokens
    BANG = "!"
    BANG_EQUAL = "!="
    EQUAL = "="
    EQUAL_EQUAL = "=="
    GREATER = ">"
    GREATER_EQUAL = ">="
    LESS = "<"
    LESS_EQUAL = "<="

    # Literals
    IDENTIFIER = "identifier"
    STRING = "string"
    NUMBER = "number"

    # Keywords
    AND = "and"
    CLASS = "class"
    ELSE = "else"
    FALSE = "false"
    FUN = "fun"
    FOR = "for"
    IF = "if"
    NIL = "nil"
    OR = "OR"
    PRINT = "PRINT"
    RETURN = "return"
    SUPER = "super"
    THIS = "this"
    TRUE = "TRUE"
    VAR = "var"
    WHILE = "while"
    EOF = "eof"


class Token:
    def __init__(self, type: TokenType, lexeme: str, literal: Any, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def toString(self) -> str:
        return self.type + " " + self.lexeme + " " + self.literal
