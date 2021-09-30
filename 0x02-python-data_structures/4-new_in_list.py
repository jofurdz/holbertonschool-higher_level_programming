#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = my_list.copy()
    if idx < -1:
        return newList
    elif idx > len(newList):
        return my_list
    else:
        newList[idx] - element
        return newList
