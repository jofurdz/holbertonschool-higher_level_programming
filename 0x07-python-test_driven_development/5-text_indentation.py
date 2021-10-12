#!/usr/bin/python3
"""prints newlines after specific characters"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for x in text:
        if x == ' ' and remove_space is True:
            continue
        elif x == '.' or x == '?' or x == ':':
            print("{}\n".format(x))
            remove_space = True
        else:
            print(x, end="")
            remove_space = False
