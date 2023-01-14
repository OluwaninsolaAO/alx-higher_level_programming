#!/usr/bin/python3
"""
A unit test module for testing ``models/base.py`` module.
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """
    This class test ``Base`` Class and its basic
    attributes.
    """

    def test_base_with_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b1.id + 1)

    def test_base_with_None_mixed(self):
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)
        self.assertEqual(b3.id, b1.id + 2)
        self.assertEqual(b3.id, b2.id + 1)

    def test_base_defined_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_base_id_collision(self):
        b1 = Base(14)
        b2 = Base(14)
        self.assertEqual(b1.id, b2.id)


if __name__ == '__main__':
    unittest.main()
