#!/usr/bin/python3
"""class Base"""


import json


class Base:
    """instances that define Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init object id"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = self

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def xyValidator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def to_json_string(list_dictionaries):
        """returns JSON representation of list of dictionaries"""
        newList = []
        if list_dictionaries == None:
            return newList
        if list_dictionaries == "":
            return newList
        else:
            newList = json.dumps(list_dictionaries)
        return newList
