#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os.path
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_save(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)


    def test_to_dict_returns_dictionary_representation(self):
        dictionary = self.base_model.to_dict()

        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['__class__'], 'BaseModel')
        self.assertEqual(dictionary['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(dictionary['updated_at'], self.base_model.updated_at.isoformat())

    def test_str_returns_string_representation(self):
        string_representation = str(self.base_model)

        self.assertIsInstance(string_representation, str)
        self.assertIn('BaseModel', string_representation)
        self.assertIn(self.base_model.id, string_representation)


if __name__ == '__main__':
    unittest.main()
