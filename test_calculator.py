import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)

    def test_odejmowanie(self):
        r = calculate(2, 1, '-')
        self.assertEqual(r, 1)

    def test_mnozenie(self):
        r = calculate(2, 5, '*')
        self.assertEqual(r, 10)

    def test_dzielenie(self):
        r = calculate(10, 2, '/')
        self.assertEqual(r, 5)

    def test_modulo(self):
        r = calculate(5, 2, '%')
        self.assertEqual(r, 1)

    def test_potegi(self):
        r = calculate(2, 2, '**')
        self.assertEqual(r, 4)
