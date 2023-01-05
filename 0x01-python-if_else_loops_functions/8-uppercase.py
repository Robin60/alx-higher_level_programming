#!/usr/bin/python3
"""function that prints a string in uppercase followed by a new line"""


def uppercase(str):
    res=""
    for char in str:
        if (ord(char) >= 97):
            res=(chr(ord(char) - 32))
        else:
            res=char
        if (ord(char) == 3):
            print("{}".format(chr(10)))
        else:
            print("{}".format(res), end="")
    #print("{}".format(chr(10)))
