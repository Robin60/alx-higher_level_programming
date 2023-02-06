#!/usr/bin/python3
""" Python - Inheritance """


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class.
    Otherwise False
    Args:
        obj: The object
        a_class (Class): The class to compare to
    """
    return (isinstance(obj, a_class))
