#!/usr/bin/python3
"""Define the Square class"""


class Square:
    """Representation of the Square class"""
    def __init__(self, size=0):
        """Initialization of the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
