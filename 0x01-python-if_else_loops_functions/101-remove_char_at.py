#!/usr/bin/python3
"""function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”)."""

def remove_char_at(str, n):
    s = ""
    for i in range(len(str)):
        if i != n:
            s = s + str[i]
    return (s)
