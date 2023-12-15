import unittest
from app.calculator import Calculator


class TestingCalculator(unittest.TestCase):
    def test_addition_positive(self):
        my_calculator = Calculator(12, 5)
        result = my_calculator.addition()
        self.assertEqual(result, 17)

    def test_addition_negative(self):
        my_calculator = Calculator(-30, -5)
        result = my_calculator.addition()
        self.assertEqual(result, -35)
