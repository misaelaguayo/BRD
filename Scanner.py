from TokenType import *
from typing import Any
from Lox import Lox

class Scanner:
    def __init__(self, source: str):
        self.tokens = []
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.keywords = {
                "and": TokenType.AND,
                "class": TokenType.CLASS,
                "else": TokenType.ELSE,
                "false": TokenType.FALSE,
                "for": TokenType.FOR,
                "fun": TokenType.FUN,
                "if": TokenType.IF,
                "nil": TokenType.NIL,
                "or": TokenType.OR,
                "print": TokenType.PRINT,
                "return": TokenType.RETURN,
                "super": TokenType.SUPER,
                "this": TokenType.THIS,
                "true": TokenType.TRUE,
                "var": TokenType.VAR,
                "while": TokenType.WHILE
                }

    def addToken(self, _type: TokenType, literal: Any = None) -> None:
        text = self.source[self.start: self.current + 1]
        self.tokens.append(Token(_type, text, literal, self.line))

    def isAtEnd(self):
        return self.current >= len(self.source)

    @staticmethod
    def isDigit(c: str) -> bool:
        return c >= '0' and c <= '9'

    @staticmethod
    def isAlpha(c: str) -> bool:
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == "_"

    @staticmethod
    def isAlphaNumeric(c: str) -> bool:
        return Scanner.isAlpha(c) or Scanner.isDigit(c)

    def identifier(self) -> None:
        while Scanner.isAlphaNumeric(self.peek()):
            self.advance()
        text: str = self.source[self.start: self.current + 1]
        type: TokenType = self.keywords[text]
        if not type:
            type = TokenType.IDENTIFIER
        self.addToken(type)

    def number(self) -> None:
        while Scanner.isDigit(self.peek()):
            self.advance()
        if self.peek() == "." and Scanner.isDigit(self.peekNext()):
            # consume the "."
            self.advance()
            while Scanner.isDigit(self.peek()):
                self.advance()
        self.addToken(TokenType.NUMBER, int(self.source[self.start: self.current + 1]))

    def string(self) -> None:
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        if self.isAtEnd():
            Lox.error(self.line, "Unterminated string")
            return
        self.advance()
        value: str = self.source[self.start + 1: self.current]
        self.addToken(TokenType.STRING, value)

    def match(self, expected: str) -> bool:
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

    def peek(self) -> str:
        if self.isAtEnd():
            return '\0'
        return self.source[self.current]

    def peekNext(self) -> str:
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current]


    def advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def scanToken(self) -> None:
        c = self.advance()
        match c:
            case TokenType.LEFT_PAREN | TokenType.RIGHT_PAREN | TokenType.LEFT_BRACE | TokenType.RIGHT_BRACE | TokenType.COMMA | TokenType.DOT | TokenType.MINUS | TokenType.PLUS | TokenType.SEMICOLON | TokenType.STAR: 
                self.addToken(c)
            # Two-char tokens
            case TokenType.BANG:
                self.addToken(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case TokenType.EQUAL:
                self.addToken(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case TokenType.LESS:
                self.addToken(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case TokenType.GREATER:
                self.addToken(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            # comments
            case TokenType.SLASH:
                if self.match('/'):
                    while self.peek() != '\n' and not self.isAtEnd():
                        self.advance()
                elif self.match('*'):
                    while self.peek() != '*' and self.peekNext() != '/' and not self.isAtEnd():
                        if self.peek() == '\n':
                            self.line += 1
                        self.advance()
                else:
                    self.addToken(TokenType.SLASH)
            # whitespace
            case ' ' | '\r' | '\t':
                ...
            case '\n':
                self.line += 1
            case '"':
                self.string()
            case _:
                if Scanner.isDigit(c):
                    self.number()
                elif Scanner.isAlpha(c):
                    self.identifier()
                else:
                    Lox.error(self.line, "Unexpected character.")


    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        # we've finished scanning. Append an EOF token
        self.tokens.append(Token(TokenType.EOF, "", {}, self.line))
        return self.tokens

