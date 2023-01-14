#!/usr/bin/python3
"""
A unit test module for testing ``models/base.py`` module.
"""
import unittest
from models.base import Base  # import Base class


class TestBase(unittest.TestCase):
    def test_base(self):
        tmp = Base()
        self.assertEqual(tmp.id, 1)


if __name__ == '__main__':
    unittest.main()
