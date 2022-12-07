#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    low = 0
    high = len(my_list) -1

    while low <= high:
        middle = (low + (high - low)) / 2

        if my_list[middle] == search:
            copy.append(replace)
        elif my_list[middle] < search:
            copy.append(my_list[low])
            low = middle + 1
        else:
            copy.append(my_list[high])
            high = middle -1
    return copy
