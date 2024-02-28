#!/usr/bin/python3
"""User tests"""


import unittest
from models.user import User

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "Hamid"
        self.user.last_name = "Hamidbayli"

    def test_email(self):
        self.assertEqual(self.user.email, "test@example.com")

    def test_password(self):
        self.assertEqual(self.user.password, "password123")

    def test_first_name(self):
        self.assertEqual(self.user.first_name, "Hamid")

    def test_last_name(self):
        self.assertEqual(self.user.last_name, "Hamidbayli")
