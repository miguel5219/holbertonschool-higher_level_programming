#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        _lastdigit = (-1 * number) % 10
    else:
        _lastdigit = number % 10

    print(_lastdigit, end='')
    return(_lastdigit)
