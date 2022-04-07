from sys import prefix
from prefix import Prefix

# calls the methods inside the prefix class to check if it can be converted or not


class PrefixToInfix():
    prefix: Prefix

    def __init__(self, prefix: Prefix) -> None:
        self.prefix = prefix

    def convertPrefixToInfix(self):
        if (not self.prefix.completePrefix()) or (not self.prefix.isPrefix()) or (not self.prefix.operatorLessThanOperand()) or (self.prefix.containsSpecialChar()):
            print("Invalid prefix expression.")
        else:
            print(self.prefixtoinfix(self.prefix.getPrefix()))

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

    def isOperator(self, symbol):
        return symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/' or symbol == '^'
