#!/usr/bin/python3
"""Define the class Rectangle"""


class Rectangle:
    """Represents class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of the class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set/get the height of class Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/get height of class Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        perimeter = ((self.__width + self.__height) * 2)
        return perimeter
        if (height or width == 0):
            return perimeter == 0
