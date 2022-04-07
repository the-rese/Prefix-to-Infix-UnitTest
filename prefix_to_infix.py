import re
# calls the methods inside the prefix class to check if it can be converted or not


class PrefixToInfix():
    prefix: str = None

    def __init__(self, prefix: str) -> None:
        self.prefix = prefix

    # c1: Should contain both operator(s) AND at least 2 operands
    def completePrefix(self):
        return (self.countOperators() >= 1) and (self.countOperands() >= 2)

    # c3: After the last operand, an operator must not be found
    def isPrefix(self):
        lastChar = self.prefix[len(self.prefix)-1]
        return not self.isOperator(lastChar)

    # c4: Number of operator(s) must not exceed or equal to the number of operands
    def operatorLessThanOperand(self):
        return self.countOperators() < self.countOperands()

    # c5: Should not contain special characters such as “!”, “$”, etc.
    def noSpecialChar(self):
        flag = True
        special_char = re.compile('[!@_#$%&)(><?\|}{~:]')

        if(special_char.search(self.prefix) != None):
            flag = False

        return flag

    def isValidExpression(self):
        if self.meetRequirements():
            return True
        else:
            print("Invalid prefix expression")
            return False

    def convertPrefixToInfix(self):
        if not self.meetRequirements():
            return False
        else:
            print(self.prefixtoinfix(self.prefix))
            return True

    #
    #
    #
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

    def meetRequirements(self):
        flag = False
        if (self.completePrefix()) and (self.isPrefix()) and (self.operatorLessThanOperand()) and (self.noSpecialChar()):
            flag = True

        return flag

    def isOperator(self, symbol):
        return symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/' or symbol == '^'

    def prefixtoinfix(self, prefix):
        stack = []
        prefix_split = prefix.split()

        i = len(prefix_split) - 1
        while i >= 0:
            if self.isOperator(prefix_split[i]):
                operand1 = stack.pop()
                operand2 = stack.pop()
                temp_str = operand1 + " " + prefix_split[i] + " " + operand2
                stack.append(temp_str)
            else:
                stack.append(prefix_split[i])

            i -= 1

        return stack.pop()
