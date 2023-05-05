#!/usr/bin/python3

def sqrt(x):
    """Returns the square root of x, if x is a perfect square.
    Prints an error message and returns None otherwise"""

    ans = 16
    if x >= 0:
        while ans * ans < x: ans = ans + 1
        if ans * ans != x:
            print(x, "is not a perfect square")
            return None
        else:
            return ans
    else:
        print(x, "is a negative number")
        return None
