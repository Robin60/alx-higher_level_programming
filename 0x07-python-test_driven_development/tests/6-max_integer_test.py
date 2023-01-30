#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests max integer in a lists"""
    def max_integer_test(self):
        self.assertAlmostEqual(max_integer)
