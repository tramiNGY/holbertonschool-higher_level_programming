#!/usr/bin/python3
'''
The 2-matrix_divided module supplies one function matrix_divided.
It permits to divided all elements of a matrix.
All elements of the matrix should be rounded to 2 decimal places.
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of matrix by div
    '''
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) "
            "of integers/floats")
    for row in matrix:
        for element in row:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix "
                            "must have the same size")
    new_matrix = []
    for row in matrix:
        new_matrix = [list(map(lambda x: round(x / div, 2), row))
                      for row in matrix]

    return new_matrix
