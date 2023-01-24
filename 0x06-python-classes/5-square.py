#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a square.
        Args:
            size (int): The size of a new square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise valueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character"""
        for i in range(0, self.__size):
            [print("#", end="") for i in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
