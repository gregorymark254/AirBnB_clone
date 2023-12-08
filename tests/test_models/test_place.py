#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''Class place test case'''

    def setUp(self):
        self.place = Place


if __name__ == '__main__':
    unittest.main()
