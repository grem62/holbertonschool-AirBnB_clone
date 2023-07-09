#!/usr/bin/pyhton3
"""Unittests module for BaseModel"""


import unittest
import os
from datetime import datetime

import models
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""

    def test_id(self):
        """Test the id attribute"""
        base = BaseModel()
        self.assertEqual(str, type(base.id))

    def test_created_at(self):
        """Test created_at attribute"""
        base = BaseModel()
        self.assertIsInstance(base.created_at, datetime)

        base.created_at = datetime.now()
        self.assertIsNotNone(base.created_at)

    def test_updated_at(self):
        """Test updated_at attribute"""
        base = BaseModel()
        self.assertIsInstance(base.updated_at, datetime)

        base.created_at = datetime.now()
        self.assertIsNotNone(base.updated_at)

    def test__str__(self):
        """Test __str__ method"""
        self.assertEqual(str, type(BaseModel.__str__(self)))

    def test_save(self):
        """Test save method"""
        base = BaseModel()
        base.name = "MyModel"
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

        with open("file.json", "r", encoding='utf-8') as f:
            self.assertIn(base.name, f.read())


    if __name__ == '__main__':
        unittest.main()
