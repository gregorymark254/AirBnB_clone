import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_uuid_generation(self):
        # Create an instance of BaseModel
        instance1 = BaseModel()
        instance2 = BaseModel()

        # Check if 'id' attribute exists
        self.assertTrue(hasattr(instance1, 'id'))
        self.assertTrue(hasattr(instance2, 'id'))

        # Check if 'id' attribute is a string
        self.assertIsInstance(instance1.id, str)
        self.assertIsInstance(instance2.id, str)

        # Check if 'id' attributes of two instances are not the same (UUID should be unique)
        self.assertNotEqual(instance1.id, instance2.id)

if __name__ == '__main__':
    unittest.main()
