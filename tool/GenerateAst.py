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
            output.write(f"\tdef visit{typeName}{baseName}(self, {baseName.lower()}):\n")
            output.write("\t\t...\n")
            output.write("\n")

    def defineAst(self, outputDir: str, baseName: str, types: List[str]) -> None:
        path = outputDir + "/" + baseName + ".py"
        print(f"writing to {path}")
        with open(path, "w", encoding="utf-8") as output:
            output.write("# Automatically generated using tool/GeneratedAst.py\n")
            output.write(f"# {types}\n\n")
            output.write("from abc import ABC, abstractmethod\n")
            output.write("from TokenType import *\n")
            output.write("from typing import Any\n\n")
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
        self.defineAst(outputDir, "Stmt", ["Expression| expression: Expr", "Print| expression: Expr"])
        self.defineAst(outputDir, "Expr", ["Binary| left: Expr,operator: Token,right: Expr", "Grouping| expression: Expr", "Literal| value: Any", "Unary| operator: Token,right: Expr"])
GenerateAst()
