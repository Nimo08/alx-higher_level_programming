#!/usr/bin/python3
"""
Unittest for base
"""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Contains unit tests for the Base class.
    """

    def test_base_id(self):
        """
        Test id.
        """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base()
        self.assertEqual(obj3.id, 3)
        obj4 = Base(12)
        self.assertEqual(obj4.id, 12)
        obj5 = Base()
        self.assertEqual(obj5.id, 4)

    def test_to_json_string(self):
        """
        Tests to_json_string method.
        """
        obj1 = Square(10, 2, 8)
        dict_sq = obj1.to_dictionary()
        json_dict_sq = Base.to_json_string([dict_sq])
        json_dict_sq_1 = Base.to_json_string([])
        json_dict_sq_2 = Base.to_json_string(None)
        self.assertEqual(type(json_dict_sq), str)
        from_json = json.loads(json_dict_sq)
        self.assertEqual(json_dict_sq_1, "[]")
        self.assertEqual(json_dict_sq_2, "[]")
        self.assertDictEqual(from_json[0], dict_sq)
        obj = Rectangle(10, 7, 2, 8)
        dictionary = obj.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_dictionary_1 = Base.to_json_string([])
        json_dictionary_2 = Base.to_json_string(None)
        self.assertEqual(type(json_dictionary), str)
        from_json = json.loads(json_dictionary)
        self.assertEqual(json_dictionary_1, "[]")
        self.assertEqual(json_dictionary_2, "[]")
        self.assertDictEqual(from_json[0], dictionary)

    def test_save_to_file(self):
        """
        Tests save_to_file method.
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            from_json = json.load(file)
            self.assertEqual(from_json, [])
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            from_json = json.load(file)
            self.assertEqual(from_json, [])
        obj1 = Rectangle(10, 7, 2, 8)
        obj2 = Rectangle(2, 4)
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            from_json = json.load(file)
            self.assertEqual(from_json, [])
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            from_json = json.load(file)
            self.assertEqual(from_json, [])
        Rectangle.save_to_file([obj1, obj2])
        with open("Rectangle.json", "r") as file:
            content = (file.read())
            from_json = json.loads(content)
            self.assertEqual(from_json[0], obj1.to_dictionary())
            self.assertEqual(from_json[1], obj2.to_dictionary())

    def test_from_json_string(self):
        """
        Tests from_json_string method.
        """
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, list_input)
        json_list_input = Rectangle.to_json_string([])
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_create(self):
        """
        Tests create method.
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual((r1 is r2), False)
        self.assertEqual((r1 == r2), False)
        s1 = Square(2, 1, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual((s1 is s2), False)
        self.assertEqual((s1 == s2), False)

    def test_load_from_file(self):
        """
        Tests load_from_file method.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rect_input = [r1, r2]
        Rectangle.save_to_file(list_rect_input)
        list_rect_output = Rectangle.load_from_file()
        for i in range(2):
            self.assertEqual(str(list_rect_input[i]), str(list_rect_output[i]))
            self.assertNotEqual(list_rect_input[i], list_rect_output[i])
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_sq_input = [s1, s2]
        Square.save_to_file(list_sq_input)
        list_sq_output = Square.load_from_file()
        for i in range(2):
            self.assertEqual(str(list_sq_input[i]), str(list_sq_output[i]))
            self.assertNotEqual(list_sq_input[i], list_sq_output[i])

    def tearDown(self):
        """
        Deallocating resources.
        """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
