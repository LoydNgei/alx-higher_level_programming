#!/usr/bin/python3
"""Define a class square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of the class Square"""

    def __init__(self, size):
        """Initialization of the class Square
        Args:
            size (int): The size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
