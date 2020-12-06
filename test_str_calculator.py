import unittest

from str_calculator import str_calculate

class TestStringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculate("a", "b", 'concat')
        self.assertEqual(r, 'ab')

    def test_konczysie(self):
        r = str_calculate("zima", "ma", 'end')
        self.assertEqual(r, True)

    def test_zawiera(self):
        r = str_calculate("Jaka pogoda", "Ja", 'contain')
        self.assertTrue(r)
        r = str_calculate("XYZ", "abc", 'contain')
        self.assertFalse(r)

    def test_start(self):
        r = str_calculate("Wesoly dzien", "We", 'start')
        self.assertEqual(r, True)
