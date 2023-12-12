#!/usr/bin/python3
import json
from os.path import isfile


class FileStorage:
    '''
    Serializes instances to a JSON file
    and deserializes JSON file to instances.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        ser_obj = {}
        for key, obj in self.__objects.items():
            ser_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(ser_obj, file)

    def reload(self):
        '''
        deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist,no exception should be raised)
        '''
        with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            for key, value in data.items():
                # Ensure the key is a string in the format "ClassName.id"
                if '.' in key:
                    class_name, _ = key.split('.', 1)
                    # Check if the class exists before
                    # attempting to create an instance
                    if class_name in globals():
                        cls_obj = globals()[class_name]
                        instance = cls_obj(**value)
                        FileStorage.__objects[key] = instance

    def classes(self):
        '''Returns a list of class names.'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
        }
        return classes


# Creating an instance for file storage
storage = FileStorage()
storage.reload()
