#!/usr/bin/python3
"""Define class that inherits"""


class MyList(list):
    """Class MyList that inherits from list."""
    def __init___(self):
        """Initialization of the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
