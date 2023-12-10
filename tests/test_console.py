#!/usr/bin/python3
import unittest
from models.engine.file_storage import storage


class TestConsole(unittest.TestCase):
    '''class Console test case'''

    def setUp(self):
        self.console = storage


if __name__ == '__main__':
    unittest.main()
