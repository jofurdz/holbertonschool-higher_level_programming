#!/usr/bin/python3
"""returns the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """returns JSON representation"""
    return json.dumps(my_obj)
