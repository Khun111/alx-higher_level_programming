#!/usr/bin/python3
'''Module for a function that returns a list of lists\
of integers representing the Pascal’s triangle'''


def pascal_triangle(n):
    '''A function that returns a list of lists of\
integers representing the Pascal’s triangle'''
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(n - 1):
        inner = pascal[-1]
        tmp = [1]
        for j in range(i):
            tmp.append(inner[j] + inner[j + 1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal
