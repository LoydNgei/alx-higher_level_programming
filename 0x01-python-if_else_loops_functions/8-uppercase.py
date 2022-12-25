#!/usr/bin/python3
"""Function that prints a string in uppercase followed by new line"""

def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
