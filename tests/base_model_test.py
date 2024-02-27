#!/usr/bin/python3
"""Base class tests"""

import unittest
from models.base_model import BaseModel


class TestStringMethods(unittest.TestCase):
    def test_init(self):
        instance = BaseModel()

        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.updated_at)
        self.assertIsNotNone(instance.created_at)

    def test_save(self):
        instance = BaseModel()

        old_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertEqual(model_dict, dict)
        self.assertEqual(model_dict.id, model.id)
        self.assertEqual(model_dict.created_at, model.created_at.isoFormat())
        self.assertEqual(model_dict.updated_at, model.updated_at.isoFormat())

    def test_str(self):
        model = BaseModel()
        print(model)
        self.assertIn(model.id, str(model))
        #self.assertIn(model)
