#!/usr/bin/python3
def max_integer(my_list=[]):
    store = my_list[0]
    if my_list:
        for x in my_list:
            if x > store:
                store = x
    else:
        return None
    return store
