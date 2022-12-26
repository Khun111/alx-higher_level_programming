#!/usr/bin/python3
'''Module to divide a matrix contents'''
def matrix_divided(matrix, div):
    '''Function we're using'''
    if not [isinstance(num, (int, float)) for num in matrix]:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')