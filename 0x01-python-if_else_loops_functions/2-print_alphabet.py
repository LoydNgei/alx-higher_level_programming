#!/usr/bin/python3
"""Prints the ASCII alphabet in lowercase, Not followed by a new line"""

for i in range(97, 123):
    print(str.format(chr(i)), end="")
