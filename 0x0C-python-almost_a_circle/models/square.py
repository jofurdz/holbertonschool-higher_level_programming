#!/usr/bin/python3
"""class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__ (self):
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        return "[Square] ({}) {}/{} - {}".format(i, x, y, w)
