#!/usr/bin/python3
"""Prints numbers from 0 - 99(2 digits, separated by (,))"""

for num in range(00, 100):
    print("{:02d}".format(num), end="\n" if num == 99 else (", "))
