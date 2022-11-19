# Automatically generated using tool/GeneratedAst.py
# ['Binary| left: Expr, operator: Token,right: Expr ', 'Literal| value: Any', 'Unary| operator: Token,right: Expr']

from TokenType import *
from typing import Any
class Expr:
	...
class Binary(Expr):
	def __init__(self, left: Expr, operator: Token,right: Expr):
		self.left=left
		self. operator= operator
		self.right=right

class Literal(Expr):
	def __init__(self, value: Any):
		self.value=value

class Unary(Expr):
	def __init__(self, operator: Token,right: Expr):
		self.operator=operator
		self.right=right

