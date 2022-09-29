#!/usr/bin/python3
# function that returns a key with the biggest integer value.


def best_score(a_dictionary):
    maximum = 0

    if not a_dictionary:
        return (None)

    for key, value in a_dictionary.items():
        if value > maximum:
            bestKey = key
            maximum = value
    return bestKey
