#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.
        Args:
            size (int): The size of a new square
            position (int, int): the position of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set current positiom of the square. """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of square"""
        if (!isinstance(value, tuple) |
                len(value) != 2 |
                not all(isinstance(n, int) for n in value) |
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self._position[1])]
        for i in range(0, self.__size):
            [print("", end=""), for j in range(0, slf.__position[0])]
            [print("#", end=""), for k in range(self.__size)]
            print("")
