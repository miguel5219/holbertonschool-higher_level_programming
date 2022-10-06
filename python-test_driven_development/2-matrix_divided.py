#!/usr/bin/python3
"""
divide a matrix
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    the function divides the elements of
    a matrix and returns to a new matrix
    """

    mat_len = len(matrix[0])

    for col in matrix:
        if len(col) != mat_len:
            raise TypeError("Each row of the matrix must have the same size")
        for row in col:
            if type(row) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return (list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)))