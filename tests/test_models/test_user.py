#!/usr/bin/python3
"""User tests"""


import unittest
import os

from models.user import User
from models import storage


class TestUserModel(unittest.TestCase):
    def setUp(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage.__objects = {}

        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "Hamid"
        self.user.last_name = "Hamidbayli"

    def test_type(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_user_attributes(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "Hamid")
        self.assertEqual(self.user.last_name, "Hamidbayli")
