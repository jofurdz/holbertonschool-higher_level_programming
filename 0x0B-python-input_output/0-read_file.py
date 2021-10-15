#!/usr/bin/python3
"""reads a file and prints it to stdout"""


def read_file(filename=""):
    """reads file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
