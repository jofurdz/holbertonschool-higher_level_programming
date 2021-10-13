#!/usr/bin/python3
"""creates class BaseGeometry"""


class BaseGeometry:
    """instance that raises exception"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value's type and value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
