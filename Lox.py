import sys

class Lox:
    def run(self, source: str) -> None:
        tokens = source.split(" ")
        for token in tokens:
            print(token)

    def runPrompt(self):
        while True:
            line = input("> ")
            if not line:
                break
            self.run(line)

    def runFile(self, path: str) -> None:
        raise NotImplementedError("Has not been implemented yet!")

    def __init__(self) -> None:
        self.hadError = False

        if len(sys.argv) > 2:
            raise Exception("Usage:plox [script]")
            return
        elif len(sys.argv) == 2:
            self.runFile(sys.argv[0])
        else:
            self.runPrompt();

Lox()
