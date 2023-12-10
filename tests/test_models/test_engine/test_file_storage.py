# #!/usr/bin/python3
# import unittest
# import os
# from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel


# class TestFileStorage(unittest.TestCase):
#     '''Class Filestorage test case'''

#     def setUp(self):
#         self.fileStorage = FileStorage

#     def tearDown(self):
#         # Remove the JSON file after each test
#         if os.path.isfile(self.file_storage._FileStorage__file_path):
#             os.remove(self.file_storage._FileStorage__file_path)

#     def test_all(self):
#         # Test the all method to ensure it returns the __objects dictionary
#         result = self.file_storage.all()
#         self.assertIsInstance(result, dict)

#     def test_new(self):
#         # Test the new method to ensure it adds an object to __objects
#         obj = BaseModel()
#         self.file_storage.new(obj)
#         key = "{}.{}".format(obj.__class__.__name__, obj.id)
#         self.assertIn(key, self.file_storage._FileStorage__objects)

#     def test_save_and_reload(self):
#         # Test the save and reload methods to ensure data consistency
#         obj = BaseModel()
#         self.file_storage.new(obj)
#         self.file_storage.save()

#         # Create a new instance of FileStorage for reloading
#         new_file_storage = FileStorage()
#         new_file_storage.reload()

#         key = "{}.{}".format(obj.__class__.__name__, obj.id)
#         self.assertIn(key, new_file_storage._FileStorage__objects)
#         reloaded_obj = new_file_storage._FileStorage__objects[key]
#         self.assertIsInstance(reloaded_obj, BaseModel)
#         self.assertEqual(reloaded_obj.id, obj.id)

#     def test_classes(self):
#         # Test the classes method to ensure it returns the expected classes
#         classes = self.file_storage.classes()
#         expected_classes = {
#             'BaseModel': BaseModel,
#             'User': BaseModel,
#             'State': BaseModel,
#             'City': BaseModel,
#             'Amenity': BaseModel,
#             'Place': BaseModel,
#             'Review': BaseModel,
#         }
#         self.assertEqual(classes, expected_classes)


# if __name__ == '__main__':
#     unittest.main()
