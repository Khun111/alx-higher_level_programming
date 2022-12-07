#!/usr/bin/python377
def square_matrix_map(matrix=[]):
    return (list(map(lambda i: list(map(lambda j: j * j, i[:])), matrix)))
