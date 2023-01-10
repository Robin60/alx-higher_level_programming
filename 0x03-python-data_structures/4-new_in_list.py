#!/usr/bin/python3
""" function that replaces an element in a list at a specific position"""


def new_in_list(my_list, idx, element):
    lcopy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return lcopy
    lcopy[idx] = element
    return lcopy
