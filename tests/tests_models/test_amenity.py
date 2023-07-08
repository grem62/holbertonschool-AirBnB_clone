#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""Unittest testing a empty string"""


class AmenityTest(unittest.TestCase):

    def test_name_attribute(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
