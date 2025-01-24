#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test Class for function max_integer
    """
    def test_max_integer(list=[]):
        """
        Returns max integer of list
        """
        list.assertEqual(max_integer([1, 2, 3, 4]), 4)
        list.assertEqual(max_integer([1, 2, 4, 2]), 4)
        list.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        list.assertEqual(max_integer([]), None)
        list.assertEqual(max_integer([1]), 1)
