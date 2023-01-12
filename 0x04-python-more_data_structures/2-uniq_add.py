#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq = []

    for x in my_list:
        if x not in uniq:
            uniq.append(x)
    sum = 0
    for val in uniq:
        sum += val
    return sum
