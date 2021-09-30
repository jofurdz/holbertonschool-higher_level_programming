#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 0
    for row in matrix:
        for value in row:
            x += 1
            if x == len(row):
                print("{:d}".format(value), end='')
                x = 0
            else:
                print("{:d}".format(value), end=' ')
        print()
