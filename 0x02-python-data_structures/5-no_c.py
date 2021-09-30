#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        newString += x
    return newString
