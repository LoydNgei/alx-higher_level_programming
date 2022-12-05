#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]
    for i in my_list:
        if my_list == 0:
            return None
        if i > largest:
            largest = i
            return largest
