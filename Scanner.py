from TokenType import *
from typing import Dict

class Scanner:
    def __init__(self, source):
        self.tokens = []
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1

    def addToken(self, _type: TokenType, literal: Dict = {}):
        text = self.source[self.start, self.current + 1]
        self.tokens.append(Token(_type, text, literal, self.line))

    def isAtEnd(self):
        return self.current >= len(self.source)


    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def scanToken(self):
        c = self.advance()
        match c:
            case TokenType.LEFT_PAREN | TokenType.RIGHT_PAREN | TokenType.LEFT_BRACE | TokenType.RIGHT_BRACE | TokenType.COMMA | TokenType.DOT | TokenType.MINUS | TokenType.PLUS | TokenType.SEMICOLON | TokenType.STAR: 
                self.addToken(c)
            case _:
                print("Error")


    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        # we've finished scanning. Append an EOF token
        self.tokens.append(Token(TokenType.EOF, "", {}, self.line))
        return self.tokens

