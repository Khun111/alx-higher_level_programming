#!/usr/bin/python3
'''Module for using numpy to multiply our matrices'''
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    '''Function to implement our lazy matrix mul'''
    return (np.matmul(m_a, m_b))