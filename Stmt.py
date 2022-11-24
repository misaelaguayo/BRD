# Automatically generated using tool/GeneratedAst.py
# ['Expression| expression: Expr', 'Print| expression: Expr']

from abc import ABC, abstractmethod
from TokenType import *
from Expr import Expr

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


