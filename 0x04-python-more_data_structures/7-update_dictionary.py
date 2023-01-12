#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    dicts = a_dictionary.copy()
    for k, v in dict.items():
        if k == key:
            a_dictionary[k] = value
        else:
            a_dictionary.update({key: value})
    return a_dictionary
