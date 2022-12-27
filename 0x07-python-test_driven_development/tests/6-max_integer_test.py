#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list of strings
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['A', 'B', 'C', 'D']), 'D')

        # Test with an empty list
        self.assertEqual(max_integer([]), None)

        # Test with a list of mixed types
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3, 4])
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 'a'])

        # Test with a list of length 1
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(['a']), 'a')
