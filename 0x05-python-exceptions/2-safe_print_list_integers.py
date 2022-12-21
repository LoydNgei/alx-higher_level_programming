#!/usr/bin/python3
'''Function that prints the first x elements of a list and only integers'''


def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            total += 1
        except (TypeError, ValueError):
            continue
    print("")
    return total
