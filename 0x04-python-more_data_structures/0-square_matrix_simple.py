#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat = [list(map(lambda x: x * x, line))for line in matrix]
    return (newmat)
