#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
from datetime import datetime

from models import storage


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            try:
                self.updated_at = datetime.strptime(kwargs.get('updated_at', ''),
                        '%Y-%m-%dT%H:%M:%S.%f')
                self.created_at = datetime.strptime(kwargs.get('created_at', ''), 
                        '%Y-%m-%dT%H:%M:%S.%f')
            except ValueError:
                # Handle datetime conversion errors here
                self.updated_at = datetime.now()
                self.created_at = datetime.now()


            #kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
            #                                         '%Y-%m-%dT%H:%M:%S.%f')
           #kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
             #                                         '%Y-%m-%dT%H:%M:%S.%f')



            kwargs.pop('__class__', None)  # Safely remove __class__ if it exists
            self.__dict__.update(kwargs)

            #del kwargs['__class__']
            #self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
