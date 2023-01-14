#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base(self):
        tmp = Base()
        self.assertEqual(tmp.id, 1)

if __name__ == '__main__':
    unittest.main()
