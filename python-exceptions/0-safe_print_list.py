#!/usr/bin/python3
# function that prints x elements of a list


def safe_print_list(my_list=[], x=0):

    number = 0
    for element in my_list:
        try:
            if x > 0:
                print(f"{element}", end="")
            else:
                break
            number += 1
            x -= 1
        except IndexError:
            break
    print()
    return number
