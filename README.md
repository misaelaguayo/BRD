# Plox

## Motivation
As part of my investigation on language design, I followed the work outlined in *crafting interpreters* by _Robert Nystrom_. The book outlines how to create a new interpreted language called *Lox*. The 
language is implemented in Java, but to make sure I understood the content I challenged myself to implement the same material but in Python. 

## Components
Plox consists of four main components to execute a program
- Lox.py - The entry point to our interpreter
- Scanner.py - Group program into tokens understood by the language
    - This is also known as *lexical analysis* in language theory. The grammar used for this step is usually a regular grammar
- Interpreter.py - Program which interprets the lox grammar. In Language theory, this is *semantic analysis*. The semantic grammar is usually *context free*
- GenerateAst.py - The creation of Nodes represented in the Abstract Syntax Tree are pretty alike. So instead of generating them ourselves, we've automated a script `GenerateAst.py` to do this for us!
- AstPrinter.py - Mainly for debugging, prints out the AST built by our program. 

## Installation and running
All you need is python to run the REPL and the interpreter

- REPL:
    - `python Lox.py` will run the REPL
- Interpreter:
    - `python Lox.py <program.plox>` will run the interpreter for a plox program
