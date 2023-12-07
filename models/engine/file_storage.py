#!/usr/bin/python3
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}
    classes = {
        'BaseModel': BaseModel,
        'User': User
    }

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        ser_obj = {key: obj.to_dict()
                   for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(ser_obj, file)

    def reload(self):
        ''' 
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        '''
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
                for key, value in data.items():
                    cls = key.split('.')[0]
                    obj = globals()[cls](**value)
                    FileStorage.__objects[key] = obj
