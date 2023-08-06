#!/usr/bin/python3
"""
Module contains matrix_mul function
matrix_mul function: multiplies matrices: m_a and m_b
and prints the result to stdout
TypeError: m_a must be a list or m_b must be a list
TypeError: m_a must be a list of lists or m_b must be a list of lists
ValueError: m_a can't be empty or m_b can't be empty
TypeError: m_a should contain only integers or
floats or m_b should contain only integers or floats
TypeError: each row of m_a must be of the same size
or each row of m_b must be of the same size
ValueError: m_a and m_b can't be multiplied
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies matrices: m_a and m_b
    Args:
        m_a: list
        m_b: list
    Return: result of multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row_x in m_a:
        if not isinstance(row_x, list):
            raise TypeError("m_a must be a list of lists")
    for row_y in m_b:
        if not isinstance(row_y, list):
            raise TypeError("m_b must be a list of lists")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    for row_x in m_a:
        for i in row_x:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row_x) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row_y in m_b:
        for j in row_y:
            if not isinstance(j, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
            if len(row_y) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
    x = len(m_a)
    y = len(m_a[0])

    p = len(m_b)
    q = len(m_b[0])

    if y != p:
        raise ValueError("m_a and m_b can't be multiplied")
    m_c = []
    for row in range(x):
        row_val = []
        for col in range(q):
            row_val.append(0)
        m_c.append(row_val)

    for i in range(x):
        for j in range(q):
            val = 0
            for a in range(y):
                val += m_a[i][a] * m_b[a][j]
            m_c[i][j] = val
    return m_c
