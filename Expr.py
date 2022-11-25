# Automatically generated using tool/GeneratedAst.py
# ['Binary| left: Expr,operator: Token,right: Expr', 'Grouping| expression: Expr', 'Literal| value: object', 'Unary| operator: Token,right: Expr', 'Variable|name: Token']

from TokenType import *
from abc import ABC, abstractmethod
class Expr(ABC):
	@abstractmethod
	def accept(self, visitor):
		...

class Visitor(ABC):
	@abstractmethod
	def visitBinaryExpr(self, expr):
		...

	@abstractmethod
	def visitGroupingExpr(self, expr):
		...

	@abstractmethod
	def visitLiteralExpr(self, expr):
		...

	@abstractmethod
	def visitUnaryExpr(self, expr):
		...

	@abstractmethod
	def visitVariableExpr(self, expr):
		...

class Binary(Expr):
	def __init__(self, left: Expr,operator: Token,right: Expr):
		self.left=left
		self.operator=operator
		self.right=right
	def accept(self, visitor):
		return visitor.visitBinaryExpr(self)


class Grouping(Expr):
	def __init__(self, expression: Expr):
		self.expression=expression
	def accept(self, visitor):
		return visitor.visitGroupingExpr(self)


class Literal(Expr):
	def __init__(self, value: object):
		self.value=value
	def accept(self, visitor):
		return visitor.visitLiteralExpr(self)


class Unary(Expr):
	def __init__(self, operator: Token,right: Expr):
		self.operator=operator
		self.right=right
	def accept(self, visitor):
		return visitor.visitUnaryExpr(self)


class Variable(Expr):
	def __init__(self, name: Token):
		self.name=name
	def accept(self, visitor):
		return visitor.visitVariableExpr(self)


