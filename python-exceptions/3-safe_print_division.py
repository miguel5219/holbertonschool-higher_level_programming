#!/usr/bin/python3
# function that divides 2 integers and prints the result.


def safe_print_division(a, b):

    try:
        prod = a / b
        print("Inside result: {:.1f}".format(prod))
    except ZeroDivisionError:
        prod = None
        print("Inside result: {}".format(prod))
    finally:
        return prod
