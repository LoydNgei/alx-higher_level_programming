#!/usr/bin/python3
"""Define a string to a text file function"""


def write_file(filename="", text=""):
    """function that write a string to textfile and returns no of characters"""
    with open(filename, "w", encoding = "utf-8") as f:
        return (f.write(text))
