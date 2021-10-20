#!/usr/bin/python3
"""class Rectangle that inherits from base"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.xyValidator("x", x)
        self.__x = x
        self.xyValidator("y", y)
        self.__y = y

    def area(self):
        """returns area"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for w in range(self.__width):
                if w == 0:
                    for x in range(self.__x):
                        print(" ", end="")
                print("#", end="")
            print()

    def __str__(self):
        """returns rectangle"""
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))

    def update(self, *args):
        """assigns argument to each attribute"""
        for x in range(len(args)):
            if x == 0:
                self.id = args[x]
            if x == 1:
                self.__width = args[x]
            if x == 2:
                self.__height = args[x]
            if x == 3:
                self.__x = args[x]
            if x == 4:
                self.__y - args[x]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.xyValidator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.xyValidator("y", value)
        self.__y = value

