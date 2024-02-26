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
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs.get(key),
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs.get(key),
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == "my_number":
                    self.my_number = kwargs.get(key)
                if key == "name":
                    self.name = kwargs.get(key)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Str method"""
        return f'[{type(self).__name__}] {self.id} {self.__dict__}'

    def save(self):
        """ Update the update_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary """
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)
