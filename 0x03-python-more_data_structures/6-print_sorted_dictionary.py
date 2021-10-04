#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newDict = a_dictionary.copy()
    for x in sorted(newDict):
        print("{}: {}".format(x, newDict[x]))
