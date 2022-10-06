#!/usr/bin/python3
"""Max integer - Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """cases"""

    def test_max_integer(self):
        list = [0, 1, 2, 3]
        self.assertEqual(max_integer(list), 3)

    def test_max_beginning(self):
        list = [66, 57, 44, 23]
        self.assertEqual(max_integer(list), 66)

    def test_max_end(self):
        list = [1, 5, 9, 21, 36]
        self.assertEqual(max_integer(list), 36)

    def test_max_middle(self):
        list = [5, 7, 46, 13, 33]
        self.assertEqual(max_integer(list), 46)

    def test_max_one_negative(self):
        list = [1, -7, 7, 9, 19]
        self.assertEqual(max_integer(list), 19)

    def test_max_only_negative(self):
        list = [-13, -46, -35, -6, -1]
        self.assertEqual(max_integer(list), -1)

    def test_max_one_element(self):
        list = [12]
        self.assertEqual(max_integer(list), 12)

    def test_max_empty(self):
        list = []
        self.assertEqual(max_integer(list), None)    
        