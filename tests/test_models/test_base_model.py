#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import ast


class Test_BaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_instance_creation(self):
        self.assertTrue(isinstance(self.model, BaseModel))
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        self.assertIsNotNone(self.model.id)
        self.assertEqual(len(self.model.id), 36)

    def test_created_at_type(self):
        self.assertTrue(isinstance(self.model.created_at, datetime))

    def test_updated_at_type(self):
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test_save(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertNotIn('_sa_instance_state', model_dict)

    def tearDown(self):
        del self.model


if __name__ == '__main__':
    unittest.main()
