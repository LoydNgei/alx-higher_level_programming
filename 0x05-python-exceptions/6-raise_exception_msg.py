#!/usr/bin/python3
'''Function that raises a name exception with a message'''


def raise_exception_msg(message=""):
    msg = message
    raise NameError(msg)
