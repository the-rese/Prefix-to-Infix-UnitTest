import re

# this class is used to check the prefix expression before converting it to infix


class Prefix():

    def __init__(self, prefix) -> None:
        self.prefix = prefix

    # c1: Should contain both operator(s) AND at least 2 operands
    def completePrefix(self):
        flag = True
        if (self.countOperators() < 1) or (self.countOperands() < 2):
            flag = False

        return flag

    # c3: After the last operand, an operator must not be found
    def isPrefix(self):
        flag = True
        lastChar = self.prefix[len(self.prefix)-1]
        special_char = ['+', '-', '*', '/', '^']
        for char in special_char:
            if char == lastChar:
                flag = False

        return flag

    # c4: Number of operator(s) must not exceed or equal to the number of operands
    def operatorLessThanOperand(self):
        return self.countOperators() < self.countOperands()

    # c5: Should not contain special characters such as “!”, “$”, etc.
    def containsSpecialChar(self):
        flag = False
        special_char = re.compile('[!@_#$%&)(><?\|}{~:]')

        if(special_char.search(self.prefix) != None):
            flag = True

        return flag

    # getter functions
    # helps in checking
    def getNumOperators(self):
        return self.countOperators()

    def getNumOperands(self):
        return self.countOperands()

    def getPrefix(self):
        return self.prefix

    # helper functions
    def countOperators(self):
        counter = 0
        for char in self.prefix:
            if (char == '+') or (char == '-') or (char == '*') or (char == '/') or (char == '^'):
                counter = counter + 1

        return counter

    def countOperands(self):
        counter = 0
        for char in self.prefix:
            if char.isdigit():
                counter = counter + 1
            elif char.isalpha():
                counter = counter + 1

        return counter
