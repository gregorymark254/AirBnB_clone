#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''Class user test case'''

    def setUp(self):
        self.user = User


if __name__ == '__main__':
    unittest.main()
