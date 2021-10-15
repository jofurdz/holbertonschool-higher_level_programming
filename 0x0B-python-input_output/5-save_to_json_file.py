#!/usr/bin/python3
"""writes an object to a text file using json"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object using json"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
