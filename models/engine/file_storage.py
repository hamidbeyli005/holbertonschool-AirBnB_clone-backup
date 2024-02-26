#!/usr/bin/python3
"""FileStorage Module"""


import os
import json
from models.base_model import BaseModel


class FileStorage():
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects = FileStorage.__objects
        my_obj = {}

        for key in objects.keys():
            my_obj[key] = objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as my_file:
            json.dump(my_obj, my_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as my_file:
                obj_dicts = json.load(my_file)
                for key, values in obj_dicts.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    instance = cls(**values)
                    FileStorage.__objects[key] = instance
