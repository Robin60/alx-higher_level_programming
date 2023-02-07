#!/usr/python3
""" Python inheritance"""


def lookup(obj):
    """ Function returns list of available attributes
    and methods.
    Args:
        obj (any): The object
    Returns:
           A list of objects
    """
    return (dir(obj))
