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

    def update(self, *args, **kwargs):
        """assigns attributes to arguments"""
        attributes = ["id", "size", "x", "y"]
        for j in range(len(args)):
            if j == 0:
                self.id = args[j]
            if j == 1:
                self.size = args[j]
            if j == 2:
                self.x = args[j]
            if j == 3:
                self.y = args[j]

        if not args:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


