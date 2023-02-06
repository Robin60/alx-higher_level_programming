#!/usr/bin/python3
""" Python - Inheritance """


class MyInt(int):
    """Custom int type inverting behavior of != and == operators.
    """

    def __eq__(self, item):
        """Reverses behaviour of == operator. """
        return (int(self) != int(item))

    def __ne__(self, item):
        """Reverses behaviour of == operator. """
        return (int(self) == int(item))
