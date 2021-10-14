#!/usr/bin/python3
"""creates class that inherits"""


class MyList(list):
    """class that inherits"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
