#!/usr/bin/python3
""" Python - Inheritance """


def add_attribute(obj, attribute, value):
    """Attempts to set or update `attribute` with 'value'
    Args:
       obj (any): object to have attribute set
       attribute (str): name of new/updated attribute
       value (any): value to set to attribute
    Raises:
        TypeError: If adding or updating attribute not possible
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
