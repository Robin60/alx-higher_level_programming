#!/usr/bin/python3
""" function that checks for lowercase character"""
def isslower(c):
    if (ord(c) >=97 and ord(c) <= 122):
        return True
    else:
        return False
