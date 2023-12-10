#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''Class state test case'''

    def setUp(self):
        self.state = State


if __name__ == '__main__':
    unittest.main()
