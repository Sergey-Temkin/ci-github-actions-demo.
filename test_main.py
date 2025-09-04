# test_main.py
# Purpose: Unit tests for functions in main.py using Python's built-in unittest.

import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_with_zero(self):
        self.assertEqual(add(10, 0), 10)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
