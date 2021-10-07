#!/usr/bin/python3
for x in range(9):
    for j in range(x + 1, 10):
        if x != 8:
            print("{}{}".format(x, j), end=", ")
        else:
            print("{}{}".format(x, j))
