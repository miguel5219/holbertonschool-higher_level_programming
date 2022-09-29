#!/usr/bin/python3
# function that returns a new dictionary with all values multiplied by 2


def multiply_by_2(a_dictionary):
    newDic = {}
    for i in a_dictionary:
        newDic[i] = a_dictionary[i] * 2
    return newDic
