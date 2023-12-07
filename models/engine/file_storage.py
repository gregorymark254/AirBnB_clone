#!/usr/bin/python3
import json
from os.path import exists


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        pass

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        pass

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        pass

    def reload(self):
        ''' 
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        '''
        pass
