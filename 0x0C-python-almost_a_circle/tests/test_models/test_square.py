#!/usr/bin/python3
"""
Unittest for square.
"""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Contains unit tests for the Square class.
    """

    def test_square_attributes(self):
        """
        Tests square attributes.
        """
        s1 = Square(2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Square(2, 0, 0, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)

    def test_size_int(self):
        """
        Tests size of int type.
        """
        s1 = Square(3)
        self.assertEqual(s1.size, 3)

    def test_size_not_int(self):
        """
        Tests size of wrong type.
        """
        with self.assertRaises(TypeError):
            s1 = Square("3")

    def test_size_zero(self):
        """
        Tests zero size.
        """
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_size_neg(self):
        """
        Tests negative size.
        """
        with self.assertRaises(ValueError):
            s1 = Square(-2)

    def test_x_int(self):
        """
        Tests x of int type.
        """
        s1 = Square(10, 3, 1)
        self.assertEqual(s1.x, 3)

    def test_x_not_int(self):
        """
        Tests x of wrong type.
        """
        with self.assertRaises(TypeError):
            s1 = Square(10, "3", 1)

    def test_x_neg(self):
        """
        Tests negative x.
        """
        with self.assertRaises(ValueError):
            s1 = Square(10, -3, 1)

    def test_y_int(self):
        """
        Tests y of int type.
        """
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.y, 1)

    def test_y_not_int(self):
        """
        Tests y of wrong type.
        """
        with self.assertRaises(TypeError):
            s1 = Square(10, 3, "1")

    def test_y_neg(self):
        """
        Tests negative y.
        """
        with self.assertRaises(ValueError):
            s1 = Square(10, 3, -1)

    def test_area(self):
        """
        Tests area of square.
        """
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)
        s2 = Square(8, 0, 0, 12)
        self.assertEqual(s2.area(), 64)
        s3 = Square(170)
        self.assertEqual(s3.area(), 28900)

    def test_display(self):
        """
        Tests display method.
        """
        import sys
        from unittest.mock import patch
        import io
        s1 = Square(2)
        output = io.StringIO()
        with patch("sys.stdout", new=output) as capturedOutput:
            s1.display()
            capturedOutput = output.getvalue()
            expected = "##\n##\n"
        self.assertEqual(capturedOutput, expected)

    def test_display_not_zero(self):
        """
        Tests display method when x and y are not zero.
        """
        import sys
        from unittest.mock import patch
        import io
        s1 = Square(2, 2)
        output = io.StringIO()
        with patch("sys.stdout", new=output) as capturedOutput:
            s1.display()
            capturedOutput = output.getvalue()
            expected = "  ##\n  ##\n"
        self.assertEqual(capturedOutput, expected)

    def test_str(self):
        """
        Tests __str__method.
        """
        s1 = Square(5)
        res = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(s1), res)
        s2 = Square(2, 2)
        res = "[Square] (2) 2/0 - 2"
        self.assertEqual(str(s2), res)

    def test_args(self):
        """
        Tests *args.
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

    def test_kwargs(self):
        """
        Tests **kwargs.
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

    def test_to_dictionary(self):
        """
        Tests to_dictionary method.
        """
        dictionary = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, dictionary)

    def test_square_none(self):
        """
        Tests for Square(None).
        """
        import json
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            from_json = json.load(file)
            self.assertEqual(from_json, [])

    def tearDown(self):
        """
        Deallocates resources.
        """
        Base._Base__nb_objects = 0


if __name__ == '__main__':
    unittest.main()
