#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix == [[]]:
        print("")
        return None

    for a in matrix:
        for b in range(len(a)):
            print("{:d}".format(a[b]), end="")
            if b != len(a) - 1:
                print("{}".format(" "), end="")
            else:
                print("{}".format(""))
