#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''Class user test case'''

    def setUp(self):
        self.user = User

    def test_default_values(self):
        # Check if the default values are set correctly
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_set_values(self):
        # Test setting values and checking if they are stored correctly
        self.user.email = "john.doe@example.com"
        self.user.password = "securepassword"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertEqual(self.user.password, "securepassword")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_inheritance(self):
        # Check if User inherits from BaseModel
        self.assertIsInstance(self.user, BaseModel)


if __name__ == '__main__':
    unittest.main()
