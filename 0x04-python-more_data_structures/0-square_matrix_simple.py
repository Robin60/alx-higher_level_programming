#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    mat = []
    lis = []

    for row in matrix:
        for col in row:
            val = col * col
            lis.append(val)
    while (lis != []):
        mat.append(lis[:3])
        lis = lis[3:]
    return mat
