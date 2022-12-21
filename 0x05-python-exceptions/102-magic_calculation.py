#!/usr/bin/python3
'''Python function that does the same as the bytecode given'''


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except RuntimeError:
            result = b + a
            break
    return result
