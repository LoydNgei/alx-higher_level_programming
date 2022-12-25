#!/usr/bin/python3
""" prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line."""

for ch in reversed(range(97, 123)):
    print("{:c}".format(ch if (ch % 2 == 0) else (ch - 32)), end='')
