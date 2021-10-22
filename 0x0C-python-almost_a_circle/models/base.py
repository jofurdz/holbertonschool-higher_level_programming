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
        """checks if int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def xyValidator(self, name, value):
        """checks if char"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON representation of list of dictionaries"""
        newList = []
        if list_dictionaries is None:
            return newList
        if list_dictionaries == "":
            return newList
        else:
            newList = json.dumps(list_dictionaries)
        return newList

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        file = cls.__name__ + ".json"
        newList = []

        for x in list_objs:
            newList.append(x.to_dictionary())

        with open(file, "w") as f:
            f.write(cls.to_json_string(newList))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation"""
        if json_string is None:
            return ([""])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of all instances"""
        filename = cls.__name__ + ".json"
        newList = []
        try:
            with open(cls.__name__, 'r') as f:
                jsonlist = cls.from_json_string(f.read())
                for x in jsonlist:
                    newList.append(cls.create(**j))
                return newList
        except FileNotFoundError:
            return []
