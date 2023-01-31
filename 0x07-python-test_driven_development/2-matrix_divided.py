#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix (list): List of lists of integers or floats
        div (int/float): The divisor
    Raises:
          TypeError: If the matrix contains non number values
          TypeError: If the matrix contains rows of different sizes
          TypeError: If the div is not int or float
          ZeroDivisionError: If div is equal to 0
    Return:
          new matrix of elements divided by div
    """

    if ((not isinstance(matrix, list)) or (matrix == []) or
        (not all(isinstance(row, list) for row in matrix)) or
        (not all(isinstance(ele, int) or isinstance(ele, float)
         for ele in [n for row in matrix for n in row]))):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by 0")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
