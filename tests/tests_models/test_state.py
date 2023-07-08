#!/usr/bin/python3


import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_name_initialization(self):
        # Crée une instance de la classe State
        state = State()

        # Vérifie que la propriété name est initialisée à une chaîne vide
        self.assertEqual(state.name, "")

    def test_name_assignment(self):
        # Crée une instance de la classe State
        state = State()

        # Assignation de la valeur "California" à la propriété name
        state.name = "California"

        # Vérifie que la propriété name a été correctement assignée à "California"
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
