import unittest
from prefix_to_infix import PrefixToInfix as pi


class TestScenario1(unittest.TestCase):
    def setUp(self) -> None:
        self.pi = pi(prefix="+ 3 5")
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def completePrefixExpression(self):
        c1 = self.pi.completePrefix()
        self.assertEqual(c1, True)

    def isPrefixExpression(self):
        c3 = self.pi.isPrefix()
        self.assertEqual(c3, True)

    def checkNumOperators(self):
        c4 = self.pi.operatorLessThanOperand()
        self.assertEqual(c4, True)

    def checkSpecialChar(self):
        c5 = self.pi.noSpecialChar()
        self.assertEqual(c5, True)

    def outputVadilityExpression(self):
        a1 = self.pi.isValidExpression()
        self.assertEqual(a1, True)

    def ouputInfixExpression(self):
        a2 = self.pi.convertPrefixToInfix()
        self.assertEqual(a2, True)


if __name__ == "__main__":
    unittest.main()
