#!/usr/bin/python3
"""Define a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""
    with open(filename) as f:
        return json.loads(f)
