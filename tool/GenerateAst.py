import sys
from typing import List


class GenerateAst:
    def defineType(self, output, baseName: str, className: str, fieldList: str) -> None:
        output.write(f"class {className}({baseName}):\n")
        output.write(f"\tdef __init__(self, {fieldList}):\n")
        fields: List[str] = fieldList.split(",")
        for field in fields:
            name = field.split(":")[0]
            output.write(f"\t\tself.{name}={name}\n")
        output.write("\tdef accept(self, visitor):\n")
        output.write(f"\t\treturn visitor.visit{className}{baseName}(self)\n")
        output.write("\n\n")

    def defineVisitor(self, output, baseName: str, types: List[str]):
        output.write(f"class Visitor(ABC):\n")
        for type in types:
            typeName: str = type.split("|")[0].strip()
            output.write("\t@abstractmethod\n")
            output.write(
                f"\tdef visit{typeName}{baseName}(self, {baseName.lower()}):\n"
            )
            output.write("\t\t...\n")
            output.write("\n")

    def defineAst(
        self,
        outputDir: str,
        baseName: str,
        types: List[str],
        extraImports: List[str] = [],
    ) -> None:
        """
        Automatically generate AST classes

        :param str outputDir: directory to write generated files to
        :param str baseName: name given to base class which other classes inherit from
        :param list[str] types: classes to be constructed which inherit from base name
        :param list[str] extraImports: if a generated class relies on other generated classes, we need to import them here
        :return: new python files to be used as types
        :rtype: None
        """

        path = outputDir + "/" + baseName + ".py"
        print(f"writing to {path}")
        with open(path, "w", encoding="utf-8") as output:
            output.write("# Automatically generated using tool/GeneratedAst.py\n")
            output.write(f"# {types}\n\n")
            if extraImports:
                for _import in extraImports:
                    output.write(f"from {_import} import *\n")
            output.write("from abc import ABC, abstractmethod\n")
            output.write("from typing import List\n")
            output.write(f"class {baseName}(ABC):\n")
            output.write(f"\t@abstractmethod\n")
            output.write(f"\tdef accept(self, visitor):\n")
            output.write("\t\t...\n\n")
            self.defineVisitor(output, baseName, types)

            for type in types:
                className = type.split("|")[0].strip()
                fields = type.split("|")[1].strip()
                self.defineType(output, baseName, className, fields)

    def __init__(self):
        if len(sys.argv) < 2:
            raise Exception("Usage: python3 GenerateAst.py <output directory>")
        outputDir = sys.argv[1]
        self.defineAst(
            outputDir,
            "Stmt",
            [
                "Block| statements: List[Stmt]",
                "Expression| expression: Expr",
                "Print| expression: Expr",
                "Var| name: Token,initializer: Expr",
            ],
            ["Expr", "TokenType"],
        )
        self.defineAst(
            outputDir,
            "Expr",
            [
                "Assign|name: Token,value: Expr",
                "Binary| left: Expr,operator: Token,right: Expr",
                "Grouping| expression: Expr",
                "Literal| value: object",
                "Unary| operator: Token,right: Expr",
                "Variable|name: Token",
            ],
            ["TokenType"],
        )


GenerateAst()
