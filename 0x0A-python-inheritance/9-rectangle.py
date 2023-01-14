#!/usr/bin/python3
"""Define a class Rectangle that  inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of the class Rectangle"""

    def __init__(self, width, height):
        """initialize a new rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the print() and str() representation of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the print() and str() representation of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
