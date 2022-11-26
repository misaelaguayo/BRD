# Automatically generated using tool/GeneratedAst.py
# ['Block| statements: List[Stmt]', 'Expression| expression: Expr', 'Print| expression: Expr', 'Var| name: Token,initializer: Expr']

from Expr import *
from TokenType import *
from abc import ABC, abstractmethod
from typing import List
class Stmt(ABC):
	@abstractmethod
	def accept(self, visitor):
		...

class Visitor(ABC):
	@abstractmethod
	def visitBlockStmt(self, stmt):
		...

	@abstractmethod
	def visitExpressionStmt(self, stmt):
		...

	@abstractmethod
	def visitPrintStmt(self, stmt):
		...

	@abstractmethod
	def visitVarStmt(self, stmt):
		...

class Block(Stmt):
	def __init__(self, statements: List[Stmt]):
		self.statements=statements
	def accept(self, visitor):
		return visitor.visitBlockStmt(self)


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


