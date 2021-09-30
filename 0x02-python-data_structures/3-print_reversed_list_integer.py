#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverseList = my_list[::-1]
    for x in range(len(reverseList)):
        print(reverseList[x])
