#!/usr/bin/python3
"""Python inheritance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry
    Args:
        width (int): Horizontal dimension of rectanlgle
        height (int): Vertical dimension of rectangle
    Attributes:
        __width (int): private x dim of rectangle
        __height (int): private y dim of rectangle
    """

    def __init__(self, width, height):
        """ Constructor initializing derived class"""
        super.integer_validator("width", width)
        self.__width = width
        super.integer_validator("height", height)
        self.__height = height
