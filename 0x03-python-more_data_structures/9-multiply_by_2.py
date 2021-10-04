#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = a_dictionary.copy()
    for x in newDict:
        newDict[x] *= 2
    return newDict
