#!/usr/python3
""" Python - Inheritance """


class BaseGemetry:
    """ A base Geometry class """

    def area(self):
        """Raises an exception
        Exceptions:
                  TypeError: raises this error when called
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validates value
        Args:
            name (str): name bound to object
            value (any): value of object
        Exceptions:
            TypeError: If value not an int
            ValueError: If value less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
