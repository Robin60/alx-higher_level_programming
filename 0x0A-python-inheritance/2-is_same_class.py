#!/usr/bin/python3
""" Python - Inheritance """


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    Otherwise False
    Args:
        obj: The object
        a_class (Class): The class to compare to
    """
    return (type(obj) == a_class)
