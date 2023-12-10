#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''Class review test case'''

    def setUp(self):
        self.review = Review


if __name__ == '__main__':
    unittest.main()
