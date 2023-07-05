#!/usr/bin/python3
""" import """
from datetime import datetime
import uuid


class BaseModel:
    """"Class that defines all common
    attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        update_at = datetime.now()

    def to_dict(self):
        dictionnaire = self.__dict__.copy()
        dictionnaire['__class__'] = self.__class__.__name__
        dictionnaire['created_at'] = self.created_at.isoformat()
        dictionnaire['updated_at'] = self.updated_at.isoformat()
        return dictionnaire
