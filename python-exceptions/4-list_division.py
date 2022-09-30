#!/usr/bin/python3
# function that divides element by element 2 lists.


def list_division(my_list_1, my_list_2, list_length):
    
    i = 0
    newList = []
    for i in range(list_length):
        try:
            list_1 = my_list_1[i]
            list_2 = my_list_2[i]
            newList.append(list_1/list_2)
        except TypeError:
            print("Wrong type")
            newList.append(0)
        except ZeroDivisionError:
            print("Division by 0")
            newList.append(0)
        except IndexError:
            print("out of range")
            newList.append(0)
        finally:
            continue
    return newList
