#!/usr/bin/python3


def common_elements(set_1, set_2):
    res = []
    for a in set_1:
        for b in set_2:
            if a == b:
                res.append(a)
    return set(res)
