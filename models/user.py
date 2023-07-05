#!/usr/bin/python3
""" User module """

from models.base_model import BaseModel


class User(BaseModel):
    """ User model from Basemodel """
    password = ""
    email = ""
    first_name = ""
    last_name = ""