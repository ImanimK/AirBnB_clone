#!/usr/bin/python3
"""
Module for the BaseModel class.
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class for the base model of the object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a BaseModel instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-value arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of a BaseModel instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of a BaseModel instance."""
        my_dict = {key: value.isoformat() if isinstance(value, datetime) else value
                   for key, value in self.__dict__.items()}
        my_dict["__class__"] = type(self).__name__
        return my_dict

