[![tests](https://github.com/misaelaguayo/BRD/actions/workflows/python-app.yml/badge.svg)](https://github.com/misaelaguayo/BRD/actions/workflows/python-app.yml)
# Brd

## Motivation
A forked repository from my implementation of Lox in python. A new language called BRD.

## Components
Brd consists of four main components to execute a program
- Brd.py - The entry point to our interpreter
- Scanner.py - Group program into tokens understood by the language
    - This is also known as *lexical analysis* in language theory. The grammar used for this step is usually a regular grammar
- Interpreter.py - Program which interprets the brd grammar. In Language theory, this is *semantic analysis*. The semantic grammar is usually *context free*
- GenerateAst.py - The creation of Nodes represented in the Abstract Syntax Tree are pretty alike. So instead of generating them ourselves, we've automated a script `GenerateAst.py` to do this for us!
- AstPrinter.py - Mainly for debugging, prints out the AST built by our program. 

## Installation and running
All you need is python to run the REPL and the interpreter

- REPL:
    - `python -m src.Brd` will run the REPL
- Interpreter:
    - `python -m src.Brd <program.brd>` will run the interpreter for a brd program
    
Some example programs are provided on the functionality of the program. The language grammar is specified in `Brd.py`
