#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    dicts = a_dictionary.copy()
    for k in a_dicts.keys():
        if k == key:
            del a_dictionary[key]
    return a_dictionary
