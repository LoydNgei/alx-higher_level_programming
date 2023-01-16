#!/usr/bin/python3
"""Define a string to a text file function"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file

    function that write a string to textfile and returns no of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
