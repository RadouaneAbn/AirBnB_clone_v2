#!/usr/bin/python3
import unittest
from models.review import Review

class Test_ReviewModel(unittest.TestCase):
    """Test review model class """

    def setUp(self):
        self.model = Review()
        self.model.save()
    
    def test_var_init(self):
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.place_id, "")
    
if __name__ == "__main__":
    unittest.main()