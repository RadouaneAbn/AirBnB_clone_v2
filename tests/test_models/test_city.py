#!/usr/bin/python3
from models.city import City
import unittest


class Test_CityModel(unittest.TestCase):
    """Test city model class"""

    def setUp(self):
        self.model = City()
        self.model.save()

    def test_var_init(self):
        self.model = City(name="")
        self.assertEqual(self.model.name, "")


if __name__ == "__main__":
    unittest.main()