#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4)





    def __str__(self):
        return f [<class name>] (<self.id>) <self.__dict__>

    def save(self):
    
    
    def to_dict(self):
  i  