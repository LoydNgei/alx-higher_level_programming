#!/usr/bin/python3
"""Define a string appending function"""


def append_write(filename="", text=""):
    """A function that appends a string
    Args:
        filename (str): The name of the file to write
        text (str): The text to write to the file
        """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
