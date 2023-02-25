class lexer:

    tolkiens = ["print", "if", "else"]
    def __init__(self, file):
        print("start")

    
    def findToken(self, line, place):
        i = place
        while i < (len(line)):
            letter = line[i]
            if self.isChar(letter):
                token = self.getNextWord(line, i)
                if token in self.tolkiens:
                    return token
                print("\nerror: token not found")
                return None
            elif self.isDigit(letter):
                token = self.getNextDigit(line, i)
                return token
            #string 
            elif letter == "\"":
                stringy = self.getNextString(line, i)
                return stringy
            # parenthetical
            elif letter == "(":
                par = self.getNextDelim(line, i)
                return par
            else:
                print("not recognized")
                i += 1

    def isChar(self, letter):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        if letter in alpha:
            return True
        return False
    
    def isDigit(self, letter):
        digs = "0123456789"
        if letter in digs:
            return True
        return False
    
    def getNextWord(self, line, place):
        word = ""
        curr = line[place]
        while self.isChar(curr) and place < len(line) - 1:
            word += curr
            curr = line[place + 1]
            place += 1
        return word

    def getNextDigit(self, line, place):
        num = ""
        curr = line[place]
        while self.isDigit(curr) and place < len(line) - 1:
            num += curr
            curr = line[place + 1]
            place += 1
        num += curr
        return num

    def getNextString(self, line, place):
        word = ""
        place += 1
        curr = line[place]
        while curr != "\"" and place < len(line):
            word += curr
            curr = line[place + 1]
            place += 1
        return word
    
    def getNextDelim(self, line, place):
        word = ""
        place += 1
        curr = line[place]
        while curr != ")" and place < len(line):
            word += curr
            curr = line[place + 1]
            place += 1
        return word


        


class tolkien:

    PRINT = 101
    IF = 102
    ELSE = 103