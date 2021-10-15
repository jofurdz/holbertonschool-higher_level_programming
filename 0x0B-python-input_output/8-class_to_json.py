#!/usr/bin/python3
"""returns description with data structure"""


import json


def class_to_json(obj):
    """returns description with data structure"""
    return vars(obj)
