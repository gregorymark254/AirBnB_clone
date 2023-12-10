#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''Class amenity test case'''

    def setUp(self):
        self.amenity = Amenity


if __name__ == '__main__':
    unittest.main()
