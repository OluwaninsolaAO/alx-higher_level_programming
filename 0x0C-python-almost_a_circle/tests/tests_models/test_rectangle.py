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

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle("12", 15)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(None, 15)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle([1, 2, 3], 15)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(3.1416, 15)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle((1, 2), 15)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(12, "15")

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(15, None)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(15, [1, 2, 3])

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(15, 3.1416)

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(15, (1, 2))

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 5, x='5')

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 5, x=None)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 5, x=(10, 5))

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 5, x=3.1416)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 5, y='5')

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 5, y=None)

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 5, y=(10, 5))

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 5, y=3.1416)

    def test_neg_width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-5, 15)

    def test_neg_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(5, -15)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 15)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(5, 0)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(10, 5, x=-5)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(10, 5, y=-10)
