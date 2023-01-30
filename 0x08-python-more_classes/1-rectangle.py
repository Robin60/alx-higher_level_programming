#!/usr/bin/python3


class Rectangle:
    """Class that defines a rectangle
    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a rectangle object"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """The __width getter
        Returns:
               _width (int): the horizontal width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """set __width value
        Args:
            value (int): with of rectangle
        Attributes:
                 __with (int): The horizontal width
        Raises:
              TypeError: If value not an int
              ValueError: If value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The __height getter
        Returns:
            _height (int): the vertical height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height value
        Args:
            value (int): value to set to vertical height
        Attributes:
                  __height (int): The vertical height
        Raises:
              TypeError: If value is not int
              ValueError: If value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
