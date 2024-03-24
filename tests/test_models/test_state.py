#!/usr/bin/python3
import unittest
from models.state import State


class test_State(unittest.TestCase):
    """ Test state model class"""

    def setUp(self):
        self.model = State()
        self.model.save()

    def test_var_init(self):
        # self.assertTrue(hasattr(self.model, "name"))
        # self.assertEqual(self.model.name, "")
        self.model = State(name="")
        self.assertEqual(self.model.name, "")


if __name__ == "__main__":
    unittest.main()
