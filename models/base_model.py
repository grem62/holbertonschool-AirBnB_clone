#!/usr/bin/python3
"""
Imports
"""
import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def __str__(self):
        """
        Return a string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self)  :
        """ Met à jour la date de mise à jour avec la date et l'heure actuelles """
        self.updated_at = datetime.now()


    def to_dict(self):
        """
        Converts the object to a dictionary representation.
        """
        dictionnaire = {}
        dictionnaire['__class__'] = self.__class__.__name__
        dictionnaire['created_at'] = self.created_at.isoformat()
        dictionnaire['updated_at'] = self.updated_at.isoformat()
        return dictionnaire

