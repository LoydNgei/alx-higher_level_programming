#!/usr/bin/python3
"""Define a python class-to-JSON function"""

def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    json.dump(obj)
    return obj.__dict__
