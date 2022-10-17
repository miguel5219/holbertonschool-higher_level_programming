#!/usr/bin/python3
""" contains the function pascal_triangle """


def pascal_triangle(n):
    """ returns a list of integers representing
    the pascal's triangle of n

    attributes:
        n (int): height of the triangle
    """

    if n <= 0:
        return ([])

    _res = [[1]]

    for i in range(n - 1):

        AuxList = [1]

        for j in range(len(_res[i]) - 1):
            AuxList.append(_res[i][j] + _res[i][j + 1])
        AuxList.append(1)
        _res.append(AuxList)
    return (_res)
