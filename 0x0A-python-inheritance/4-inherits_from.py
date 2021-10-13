#!/usr/bin/python3
"""returns True if the object is an instance of a class
that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """ returns true if from same subclass"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
