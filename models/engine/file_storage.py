#!/usr/bin/python3
import json
from os.path import isfile


class FileStorage:
    '''Serializes instances to a JSON file and deserializes JSON file to instances.'''
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
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        '''
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = key.split('.')
                    cls_obj = globals()[cls_name]
                    obj_instance = cls_obj(**value)
                    self.__objects[key] = obj_instance
