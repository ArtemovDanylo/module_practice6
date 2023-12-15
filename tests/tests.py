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

    def test_subtraction_positive(self):
        my_calculator = Calculator(20, 5)
        result = my_calculator.subtraction()
        self.assertEqual(result, 15)

    def test_subtraction_negative(self):
        my_calculator = Calculator(-12, 5)
        result = my_calculator.subtraction()
        self.assertEqual(result, -17)

    def test_multiplication_positive(self):
        my_calculator = Calculator(12, 5)
        result = my_calculator.multiplication()
        self.assertEqual(result, 60)

    def test_multiplication_negative(self):
        my_calculator = Calculator(-5, 5)
        result = my_calculator.multiplication()
        self.assertEqual(result, -25)

    def test_division(self):
        my_calculator = Calculator(25, 5)
        result = my_calculator.division()
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        my_calculator = Calculator(25, 0)
        result = my_calculator.division()
        self.assertEqual(result, "Division by zero is not allowed")

    def test_pow_positive(self):
        my_calculator = Calculator(2, 4)
        result = my_calculator.pow()
        self.assertEqual(result, 16)

    def test_pow_negative(self):
        my_calculator = Calculator(2, -2)
        result = my_calculator.pow()
        self.assertEqual(result, 0.25)