#!/usr/bin/python3
"""Base module"""


import uuid
import datetime


class BaseModel:
    """Base class"""
    def __init__(self):
        """Base class constructor"""
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        """Str method"""
        return f'[{type(self).__name__}] {self.id} {self.__dict__}'

    def save(self):
        """Save method"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Dict method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict.get('created_at').strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = obj_dict.get('updated_at').strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict
