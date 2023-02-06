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
