#!/usr/bin/python3
def search_replace(my_list, search, replace):
    _list = my_list[:]
    for i in range(len(_list)):
        if _list[i] == search:
            _list[i] = replace
    return _list
