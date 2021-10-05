#!/usr/bin/python3
""" Defines a class Square by size"""


class Square:
    """ Defines """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
