#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for col in row:
            new_matrix = col ** 2

    return new_matrix
