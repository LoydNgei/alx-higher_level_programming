#!/usr/bin/python3
def no_c(my_string):
    c_line = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(c_line))
