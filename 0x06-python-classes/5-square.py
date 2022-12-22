#!/usr/bin/python3
"""Define the class Square"""


class Square:
    """Representation of the class Square"""
    def __init__(self, size=0):
        """Initialization of the class Square"""
        self.size = size

    @property
    def size(self):
        """Get/ Set the square of the current class"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
