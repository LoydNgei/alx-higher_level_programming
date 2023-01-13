#!/usr/bin/python3
"""Define a inherited class"""


def is_kind_of_class(obj, a_class):
   """Returns True if obj is an instance of, or obj is a class instance
   that is inherited from specialized class else return False"""
   if isinstance(obj, a_class):
       return True
   return False
