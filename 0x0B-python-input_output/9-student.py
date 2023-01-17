#!/usr/bin/python3
"""Define a class student"""


class Student:
    """Representation of the class student"""
    def __init__(self, first_name, last_name, age):
        """Initialization of the class Student
        Args:
            first_name: The first name of the student
            last_name: Last name of the student
            Age: The age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the student"""
        return self.__dict__
