#!/usr/bin/python3
"""
Module contains lazy_matrix_mul function
lazy_matrix_mul function: multiplies matrices: m_a and m_b
using numpy module
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    row_error = "matrix dimensions are not compatible for multiplication"
    matrix_error = "matrix dimensions are not aligned for multiplication"
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row_x in m_a:
        if not isinstance(row_x, list):
            raise ValueError("matrix shapes are not aligned")
    for row_y in m_b:
        if not isinstance(row_y, list):
            raise ValueError("matrix shapes are not aligned")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    for row_x in m_a:
        for i in row_x:
            if not isinstance(i, (int, float)):
                raise TypeError("invalid data for einsum")
        if len(row_x) != len(m_a[0]):
            raise ValueError(row_error)
    for row_y in m_b:
        for j in row_y:
            if not isinstance(j, (int, float)):
                raise TypeError("invalid data for einsum")
            if len(row_y) != len(m_b[0]):
                raise ValueError(row_error)
    x = len(m_a)
    y = len(m_a[0])
    p = len(m_b)
    q = len(m_b[0])
    if y != p:
        raise ValueError(matrix_error)
    m_a_np = np.array(m_a)
    m_b_np = np.array(m_b)
    res = np.dot(m_a, m_b)
    return res
