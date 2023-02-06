#!/usr/python3
"""Python inheritance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry
    Args:
        size (int): dimension of square
    Attributes:
        __size (int): private x dim of square
    """

    def __init__(self, size):
        """ Constructor initializing derived class"""
        super.integer_validator("size", size)
        self._size = size

    def area(self):
        """returns square area
        Attributes:
              __size (int): lenth of square
        Returns:
               ___size ** 2
        """
        return (self.__size ** 2)
