#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, max_integer, ["x"])
        self.assertRaises(TypeError, max_integer, True)

    def test_max_integer(self):
        res = max_integer([1, 2, 3, 4])
        self.assertEqual(res, 4)
        res = max_integer([1, 103, 45, 32])
        self.assertEqual(res, 103)
        res = max_integer([-1, 0, -12, -0])
        self.assertEqual(res, 0)

    def test_single_element(self):
        res = max_integer([2])
        self.assertEqual(res, 2)

    def test_empty_list(self):
        res = max_integer([])
        self.assertIsNone(res)

    def test_zero(self):
        res = max_integer([0, 0, 0, 0, 0])
        self.assertEqual(res, 0)

    def test_large_numbers(self):
        res = max_integer([123, 45567, 43123, 987, 134])
        self.assertEqual(res, 45567)

    def test_negative_num(self):
        res = max_integer([-1, -123, -5, -10])
        self.assertEqual(res, -1)

    def test_negative_with_zero(self):
        res = max_integer([-1, -34, 0, -976, -3])
        self.assertEqual(res, 0)

    def test_multiple_max(self):
        res = max_integer([12, 34, 23, 34])
        self.assertEqual(res, 34)

    def test_multiple_not_max(self):
        res = max_integer([12, 12, 34, 23, 45])
        self.assertEqual(res, 45)

    def test_max_float(self):
        res = max_integer([23.54, 0.12, 45.12, 3.54])
        self.assertEqual(res, 45.12)

    def test_mixed_types(self):
        res = max_integer([12, -1.45, 2.13, 0])
        self.assertEqual(res, 12)

    def test_many_elements(self):
        res = max_integer([1, 2, 3, 4, 5, 78, 54, 32, 21, 345, 211, 1000, 0,
                          54, -32, 76, -87, 98, 90, 43, 40, 12, -13, 14, 15,
                          16, 17, 18, 19, -20, 21, 22, 23, -24, 25, 43, 21,
                          97, 65, 56, 45, -101, 234, 13456, 321, 543, 654,
                          765, 876, -987, -567, 354, 243, 100])
        self.assertEqual(res, 13456)


if __name__ == '__main__':
    unittest.main()
