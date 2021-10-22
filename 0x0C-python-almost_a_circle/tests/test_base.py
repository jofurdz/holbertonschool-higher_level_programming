#!/usr/bin/python3
"""unit tests for Base"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8

class TestBase(unittest.TestCase):
    """testing class Base"""

    def testInit(self):
        """testing initialization"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)


if __name__ == "__main__":
    unittest.main()
