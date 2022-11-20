# Automatically generated using tool/GeneratedAst.py
# ['Binary| left: Expr, operator: Token,right: Expr ', 'Literal| value: Any', 'Unary| operator: Token,right: Expr']

from abc import ABC, abstractmethod
from TokenType import *
from typing import Any

class Expr(ABC):
	@abstractmethod
	def accept(self, visitor):
		...

class Visitor(ABC):
	@abstractmethod
	def visitBinaryExpr(self, expr):
		...

	@abstractmethod
	def visitLiteralExpr(self, expr):
		...

	@abstractmethod
	def visitUnaryExpr(self, expr):
		...

class Binary(Expr):
	def __init__(self, left: Expr, operator: Token,right: Expr):
		self.left=left
		self. operator= operator
		self.right=right
	def accept(self, visitor):
		return visitor.visitBinaryExpr(self)


class Literal(Expr):
	def __init__(self, value: Any):
		self.value=value
	def accept(self, visitor):
		return visitor.visitLiteralExpr(self)


class Unary(Expr):
	def __init__(self, operator: Token,right: Expr):
		self.operator=operator
		self.right=right
	def accept(self, visitor):
		return visitor.visitUnaryExpr(self)


