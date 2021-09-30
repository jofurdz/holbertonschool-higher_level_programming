#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    newList = my_list.copy()
    if idx < 0:
        return newList
    elif idx > length:
        return my_list
    else:
        newList[idx] - element
        return newList
