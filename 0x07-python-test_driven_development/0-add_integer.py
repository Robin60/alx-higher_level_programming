#!/ussr/bin/python3


def add_integer(a, b=98):
    """adds 2 integers
    Args:
        a (int): First argument to add
        b (int): the second argument
    Returns:
           Sum of two values
    """

    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an intger")
    if ((not isinstance(b, int)) or (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
