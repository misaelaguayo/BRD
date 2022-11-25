from typing import Dict
from TokenType import Token

class Environment:
    def __init__(self):
        self.values: Dict[str, object] = {}

    def get(self, name: Token) -> object:
        # return value of variable
        if name.lexeme in self.values:
            return self.values[name.lexeme]
        raise RuntimeError(name, f"Undefined variable {name.lexeme}.")

    def define(self, name: str, value: object):
        # define a variable, allows for redefinition
        self.values[name] = value
