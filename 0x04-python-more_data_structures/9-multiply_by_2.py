#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    d = a_dictionary.copy()
    list_keys = list(d.keys())
    for i in list_keys:
        d[i] *= 2
    return d
