#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None

    max_int = min(my_list)
    for itr in my_list:
        if itr > max_int:
            max_int = itr
    return max_int
