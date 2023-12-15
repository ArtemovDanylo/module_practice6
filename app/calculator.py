import random
import math


class Calculator():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def division(self):
        if self.number2 != 0:
            return self.number1 / self.number2
        else:
            print("Division by zero is not allowed")

    def pow(self):
        return math.pow(self.number1, self.number2)

    def static_random_generate(a, b):
        return random.randint(a, b)