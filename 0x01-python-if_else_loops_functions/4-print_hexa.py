#!/usr/bin/python3
"""Program that prints all numbers from 0 to 98 in decimal and in hexadecimals"""
for number in range(0, 99):
    print("{:d} = 0x{:x}".format(number, number))
