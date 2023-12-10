#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Class Filestorage test case'''

    def setUp(self):
        self.fileStorage = FileStorage


if __name__ == '__main__':
    unittest.main()
