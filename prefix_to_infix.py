from sys import prefix
from prefix import Prefix


class PrefixToInfix():
    prefix: Prefix

    def __init__(self, prefix: Prefix) -> None:
        self.prefix = prefix

    def convertPrefixToInfix(self):
        completePrefix = self.prefix.completePrefix()
        isPrefix = self.prefix.isPrefix()
        operatorLessOperand = self.prefix.operatorLessThanOperand()
        containsSpecialChar = self.prefix.containsSpecialChar()

        print(completePrefix)
        print(isPrefix)
        print(operatorLessOperand)
        print(containsSpecialChar)
        if (completePrefix == False) or (isPrefix == False) or (operatorLessOperand == False) or (containsSpecialChar):
            print("Invalid prefix expression.")
        else:
            print("The infix expression is ")
