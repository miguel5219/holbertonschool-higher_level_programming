#!/usr/bin/python3
# function that divides element by element 2 lists.


def list_division(my_list_1, my_list_2, list_length):

    newList = []
    for i in range(list_length):
        try:
            prod = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            prod = 0
        except ZeroDivisionError:
            print("Division by 0")
            prod = 0
        except IndexError:
            print("out of range")
            prod = 0
        finally:
            newList.append(prod)
    return (newList9)
