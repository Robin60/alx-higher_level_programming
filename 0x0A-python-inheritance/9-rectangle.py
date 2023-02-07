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

    def area(self):
        """Returns area of a rectangle
        Attributes:
             __width (int): the x dim of rectangle
             __height (int): the y dim of rectangle
        Returns:
             __width * __height
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Prints rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
