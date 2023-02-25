from lexer import *

class parses:

    def __init__(self, file):
        self.lex = lexer(file)
        self.file = open(file, "r+")

    def interpret(self):
        line = self.file.readline()
        while line != "":
            self.findNextToken(line, 0)
            line = self.file.readline()

        
    def findNextToken(self, line, place):
        token = self.lex.findToken(line, place)
        if token == "print":
            place += len(token)
            parenthetical = self.lex.findToken(line, place)
            arr = parenthetical.split(" + ")
            for i in range (len(arr)):
                item = arr[i]
                x = self.lex.findToken(item, 0)
                if x == None:
                    return
                print(x, end="")
                if i == len(arr) - 1:
                    print("")
        elif token == "if":
            statement = eval(self.lex.findToken(line, 3))
            if (statement):
                line = self.file.readline()
                while line[0:4] == "    ":
                    self.findNextToken(line, 4)
                    line = self.file.readline()
            else:
                while line[0:4] == "    ":
                    line = self.file.readline()
                if line[0:4] == "else":
                    line = self.file.readline()
                    print(line)
                    while line[0:4] == "    ":
                        self.findNextToken(line, 4)
                        line = self.file.readline()
                    

        else:
            print("not recognized")

