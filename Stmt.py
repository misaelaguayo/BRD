# Automatically generated using tool/GeneratedAst.py
# ['Expression| expression: Expr', 'Print| expression: Expr', 'Var| name: Token,initializer: Expr']

from Expr import *
from TokenType import *
from abc import ABC, abstractmethod
class Stmt(ABC):
	@abstractmethod
	def accept(self, visitor):
		...

class Visitor(ABC):
	@abstractmethod
	def visitExpressionStmt(self, stmt):
		...

	@abstractmethod
	def visitPrintStmt(self, stmt):
		...

	@abstractmethod
	def visitVarStmt(self, stmt):
		...

class Expression(Stmt):
	def __init__(self, expression: Expr):
		self.expression=expression
	def accept(self, visitor):
		return visitor.visitExpressionStmt(self)


class Print(Stmt):
	def __init__(self, expression: Expr):
		self.expression=expression
	def accept(self, visitor):
		return visitor.visitPrintStmt(self)


class Var(Stmt):
	def __init__(self, name: Token,initializer: Expr):
		self.name=name
		self.initializer=initializer
	def accept(self, visitor):
		return visitor.visitVarStmt(self)


