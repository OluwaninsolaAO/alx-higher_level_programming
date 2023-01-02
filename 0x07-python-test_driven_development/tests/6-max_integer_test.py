#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test class for max_integer function
    to be tested
    """

    def test_max_integer(self):
        """
        Test if max integer function works
        while generating expected outputs
        """
        self.assertEqual(max_integer([1, 5, 3, 2]), 5)

    def test_max_integer_null_list(self):
        """
        Test if max integer will handle an
        empty list correctly.
        """
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
