#!/usr/bin/python3


import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_default_values(self):
        # Crée une instance de la classe User
        user = User()

        # Vérifie que les propriétés password, email, first_name et last_name sont initialisées à une chaîne vide
        self.assertEqual(user.password, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_property_assignment(self):
        # Crée une instance de la classe User
        user = User()

        # Assignation de valeurs aux propriétés password, email, first_name et last_name
        user.password = "password123"
        user.email = "john.doe@example.com"
        user.first_name = "John"
        user.last_name = "Doe"

        # Vérifie que les propriétés ont été correctement assignées
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
