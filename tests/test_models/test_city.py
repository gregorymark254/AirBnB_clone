#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''Class City test case'''

    def setUp(self):
        self.city = City()


if __name__ == '__main__':
    unittest.main()
