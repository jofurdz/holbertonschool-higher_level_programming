#!/usr/bin/python3
"""class Base"""


class Base:
    """instances that define Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init object id"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else
            self.id = self

    