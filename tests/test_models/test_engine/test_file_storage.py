import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import storage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Ensure the file.json file is removed before each test
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_all(self):
        # Test the 'all' method
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, storage._FileStorage__objects)

    def test_new(self):
        # Test the 'new' method
        instance = BaseModel()
        storage.new(instance)
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.assertIn(key, storage.all())

    def test_save_reload(self):
        # Test the 'save' and 'reload' methods
        instance = BaseModel()
        storage.new(instance)
        storage.save()
        storage.reload()
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.assertIn(key, storage.all())

    def test_classes(self):
        # Test the 'classes' method
        classes = storage.classes()
        self.assertIsInstance(classes, dict)

        expected_classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
        }

        # Verify that each expected class is present in the result
        for class_name, class_obj in expected_classes.items():
            self.assertIn(class_name, classes)
            self.assertEqual(classes[class_name], class_obj)


if __name__ == '__main__':
    unittest.main()
