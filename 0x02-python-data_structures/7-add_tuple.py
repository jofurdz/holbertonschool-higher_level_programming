#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        newTup_a = (0, 0)
    if len(tuple_a) == 1:
        newTup_a = (tuple_a[0], 0)
    if len(tuple_a) >= 2:
        newTup_a = (tuple_a[0], tuple_a[1])
    if len(tuple_b) == 0:
        newTup_b = (0, 0)
    if len(tuple_b) == 1:
        newTup_b = (tuple_b[0], 0)
    if len(tuple_b) >= 2:
        newTup_b = (tuple_b[0], tuple_b[1])
    return tuple(map(lambda x, y: x + y, newTup_a, newTup_b))
