#!/usr/bin/python3
"""Function that prints the last digit of a number"""

def print_last_digit(number):
    last_digit = int(repr(number)[-1])
    print(last_digit, end="")
    return last_digit
