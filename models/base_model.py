#!/usr/bin/python3
""" import """
from datetime import datetime
import uuid


class BaseModel:
    """"Class that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """def init str"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """string name"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save the date and time"""
        update_at = datetime.now()

    def to_dict(self):
        """dictionnary"""
        dictionnaire = self.__dict__.copy()
        dictionnaire['__class__'] = self.__class__.__name__
        dictionnaire['created_at'] = self.created_at.isoformat()
        dictionnaire['updated_at'] = self.updated_at.isoformat()
        return dictionnaire
