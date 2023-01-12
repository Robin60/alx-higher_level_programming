#!/usr/bin/python3


def search_replace(my_list, search, replace):
    lis = list(map(lampda x: replace if x == search else x, my_list))
    return lis
