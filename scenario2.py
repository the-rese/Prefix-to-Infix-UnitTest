import unittest
from prefix_to_infix import PrefixToInfix


class TestScenario2(unittest.TestCase):
    def setUp(self) -> None:
        self.pi = PrefixToInfix("^ E F $ 6")
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_complete_prefix_expression(self):
        c1 = self.pi.completePrefix()
        self.assertEqual(c1, True)

    def test_if_prefix_expression(self):
        c3 = self.pi.isPrefix()
        self.assertEqual(c3, True)

    def test_num_operators(self):
        c4 = self.pi.operatorLessThanOperand()
        self.assertEqual(c4, True)

    def test_no_special_char(self):
        c5 = self.pi.noSpecialChar()
        self.assertEqual(c5, True)

    def test_validity_expression(self):
        a1 = self.pi.isValidExpression()
        self.assertEqual(a1, True)

    def test_ouput_infix(self):
        a2 = self.pi.convertPrefixToInfix()
        self.assertEqual(a2, True)


if __name__ == "__main__":
    unittest.main()
