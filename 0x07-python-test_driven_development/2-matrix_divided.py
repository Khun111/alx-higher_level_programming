#!/usr/bin/python3
'''Module to divide a matrix contents'''


def matrix_divided(matrix, div):
    '''Function we're using'''
    if (
        not isinstance(
            matrix, list) or matrix == [] or matrix == [[]] or not all(
            isinstance(
                row, list) for row in matrix) or not all(
                    isinstance(
                        num, (int, float))) for num in [
                            num for row in matrix for num in row]):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    if [len(row) != len(matrix[0]) for row in matrix]
        raise TypeError('Each row of the matrix must have the same size')
