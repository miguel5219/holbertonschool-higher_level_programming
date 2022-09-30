#!/usr/bin/python3
# function that converts a Roman numeral to an integer.


def roman_to_int(roman_string):
    
    if not roman_string or not isinstance(roman_string, str):
        return 0

    num = 0
    sym = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    ult = 1000

    for let in roman_string:
        dig = sym[let]

        num += dig

        if ult < dig:
            num -= 2 * ult

        ult = dig

    return (num)
