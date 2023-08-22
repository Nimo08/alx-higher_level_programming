#!/usr/bin/python3
"""
Unittest for rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Contains unit tests for the Rectangle Class.
    """

    def test_rect_attributes(self):
        """
        Tests rectangle attributes.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_width_int(self):
        """
        Tests width of int type.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    def test_width_not_int(self):
        """
        Tests width of wrong type.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)

    def test_width_zero(self):
        """
        Tests zero width.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_width_neg(self):
        """
        Tests negative width.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def test_height_int(self):
        """
        Tests height of int type.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

    def test_height_not_int(self):
        """
        Tests height of wrong type.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")

    def test_height_zero(self):
        """
        Tests zero height.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)

    def test_height_neg(self):
        """
        Tests negative height.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)

    def test_x_int(self):
        """
        Tests x of int type.
        """
        r1 = Rectangle(10, 2, 3, 1)
        self.assertEqual(r1.x, 3)

    def test_x_not_int(self):
        """
        Tests x of wrong type.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, "3", 1)

    def test_x_neg(self):
        """
        Tests negative x.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -3, 1)

    def test_y_int(self):
        """
        Tests y of int type.
        """
        r1 = Rectangle(10, 2, 3, 1)
        self.assertEqual(r1.y, 1)

    def test_y_not_int(self):
        """
        Tests y of wrong type.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, "1")

    def test_y_neg(self):
        """
        Tests negative y.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 3, -1)

    def test_area(self):
        """
        Tests area of rectangle.
        """
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)
        r3 = Rectangle(170, 11)
        self.assertEqual(r3.area(), 1870)

    def test_display(self):
        """
        Tests display method.
        """
        import sys
        from unittest.mock import patch
        import io
        r1 = Rectangle(2, 2)
        output = io.StringIO()
        with patch("sys.stdout", new=output) as capturedOutput:
            r1.display()
            capturedOutput = output.getvalue()
            expected = "##\n##\n"
        self.assertEqual(capturedOutput, expected)

    def test_str(self):
        """
        Tests __str__method.
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        res = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), res)
        r2 = Rectangle(5, 5, 1)
        res = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(r2), res)

    def test_args(self):
        """
        Tests *args.
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_kwargs(self):
        """
        Tests **kwargs.
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

    def test_to_dictionary(self):
        """
        Tests to_dictionary method.
        """
        dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, dictionary)

    def test_rect_none(self):
        """
        Tests for Rectangle(None).
        """
        import json
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            from_json = json.load(file)
            self.assertEqual(from_json, [])

    def tearDown(self):
        """
        Deallocating resources.
        """
        Base._Base__nb_objects = 0


if __name__ == '__main__':
    unittest.main()
