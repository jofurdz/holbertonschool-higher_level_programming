#!/usr/bin/python3
""" Defines a class Square by size"""


class Square:
    """ Defines an object size with verification"""
    def __init__(self, size=0):
        self.size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
