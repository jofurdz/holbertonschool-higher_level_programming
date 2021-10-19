#!/usr/bin/python3
"""class Rectangle that inherits from base"""

from models.base import Base


class Rectangle(base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        