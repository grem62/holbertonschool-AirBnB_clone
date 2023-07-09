#!/usr/bin/python3
""" import """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """"Class that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """def init str"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """string name."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save the date and time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionnary"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
