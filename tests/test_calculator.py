import unittest

from src.calculator import suma, resta, multiplicar

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(suma(4.2, 3), 7.2)

    def test_resta(self):
        self.assertEqual(resta(4, 3), 1)


    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

