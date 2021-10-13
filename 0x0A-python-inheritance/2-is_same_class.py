#!/usr/bin/python3
"""returns True if object is an instance of class"""


def is_same_class(obj, a_class):
    """returns True if object is an instance of class"""
    if type(obj) == a_class:
        return True
    else:
        return False
