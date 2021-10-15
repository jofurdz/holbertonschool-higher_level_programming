#!/usr/bin/python3
"""writes string and returns number of characters"""


def write_file(filename="", text=""):
    """counts characters of string"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
