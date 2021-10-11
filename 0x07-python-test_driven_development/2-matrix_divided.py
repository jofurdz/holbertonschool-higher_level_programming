#!/usr/bin/python3
def matrix_divided(matrix, div):

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(error)
    
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error)
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError(error)

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError(error)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")      
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(number / div, 2) for number in list] for list in matrix]
