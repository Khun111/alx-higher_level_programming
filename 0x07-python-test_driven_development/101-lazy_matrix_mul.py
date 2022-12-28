#!/usr/bin/python3
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    m_a = np.array(m_a)
    m_b =np.array(m_b)
    return (np.dot(m_a, m_b))