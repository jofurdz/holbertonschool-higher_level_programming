#!/usr/bin/python3
"""returns an object represented by a JSON string"""

import json


def from_json_string(my_str):
    """does the thing from up there"""
    return json.loads(my_str)
