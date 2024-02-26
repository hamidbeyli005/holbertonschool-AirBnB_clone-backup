#!/usr/bin/python3
"""Base module"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class"""
    def __init__(self, *args, **kwargs):
        """Base class constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    kwargs[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Str method"""
        return f'[{type(self).__name__}] {self.id} {self.__dict__}'

    def save(self):
        """Save method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dict method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        # Ensure created_at and updated_at are datetime objects
        if isinstance(obj_dict['created_at'], str):
            obj_dict['created_at'] = datetime.strptime(obj_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if isinstance(obj_dict['updated_at'], str):
            obj_dict['updated_at'] = datetime.strptime(obj_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        # Now format them as strings
        obj_dict['created_at'] = obj_dict['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = obj_dict['updated_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict

