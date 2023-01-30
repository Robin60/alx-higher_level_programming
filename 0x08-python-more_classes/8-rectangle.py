#!/usr/bin/python3


class Rectangle:
    """Class that defines a rectangle

    __str__ functionality of printing
    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle object"""
        type(self).number_of_instances +=1

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

    def area(self):
        """returns the area of a rectangle
        Attributes:
               __width (int): The horizontal width
               __height (int): The vertical height
        Returns:
               Area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter f a rectangle
        Attributes:
        __width (int): the width
        __height (int): the height
        Returns:
              perimeter, 0 if either dimension is 0
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2*(self.__height + self.__width))

    def _rectangle(self):
        """Formats '#' and '\n' and draws a rectagle
        Returns:
               str (str): The string for printing rectangle
        """
        st = ""
        for i in range(self.__height):
            for j in range(self.__width):
                st += "{}".format(self.print_symbol)
            if self.__width != 0 and i < (self.__height - 1):
                st += '\n'
        return (st)

    def __str__(self):
        """Printing of instances
        Returns:
               _rectangle (str)
        """
        return self._rectangle()

    def __repr__(self):
        """Return string with use of eval()
        Returns:
                string representation of the rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    @classmethod
    def __del__(cls):
        """Decremens instances by 1 then prints message
        upon deletion  of instance
        """
        cls.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle object): first instance
            rect_2 (Rectangle object): second instance
        Raises:
              TypeError: If rect_1 or rect_2 not instance of rectangle
        Returns:
               rect_1 if greater or equal to rect_2, else rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
