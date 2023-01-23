#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return (res)
    except:
        print("Exception: {}".format(sys.exec_info()[1]), file=syss.stderr)
        return (None)
