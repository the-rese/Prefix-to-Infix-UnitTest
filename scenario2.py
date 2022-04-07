from sys import prefix
import unittest
from prefix import Prefix
from prefix_to_infix import PrefixToInfix as pi


class TestScenario2(unittest.TestCase):
    def setUp(self) -> None:
        prefix_str = "^ E F $ 6"
        self.prefix = Prefix(prefix_str)
        # pi = pi(prefix)
        return super().setUp()

    def completePrefixExpression(self):
        c1 = self.prefix.completePrefix()
        self.assertEqual(c1, True)

    def isPrefixExpression(self):
        c3 = self.prefix.isPrefix()
        self.assertEqual(c3, True)

    def checkNumOperators(self):
        c4 = self.prefix.operatorLessThanOperand()
        self.assertEqual(c4, True)

    def checkSpecialChar(self):
        c5 = self.prefix.noSpecialChar()
        self.assertEqual(c5, True)

    # def outputInfixExpression(self):
    #     return pi.convertPrefixToInfix()


if __name__ == "__main__":
    unittest.main()
