#!/usr/bin/python3
from models.city import City
import unittest


class Test_CityModel(unittest.TestCase):
    """Test city model class"""

    def setUp(self):
        self.model = City()
        self.model.save()

    def test_var_init(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.state_id, "")


if __name__ == "__main__":
    unittest.main()