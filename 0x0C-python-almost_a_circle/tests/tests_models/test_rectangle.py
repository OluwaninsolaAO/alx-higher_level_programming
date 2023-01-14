#!/usr/bin/python3
"""
A unit test module for testing 
``models/rectangle.py`` module.
"""

import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """
    This class test ``Rectangle`` Class
    with its attributes.
    """

    def test_rectangle_init(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rect_getter(self):
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rect_pos_args(self):
        r2 = Rectangle(height=10, width=8, x=10, y=20)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.width, 8)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 20)
