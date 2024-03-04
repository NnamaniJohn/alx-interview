#!/usr/bin/python3
"""
pascal triangle
"""


def get_row(n):
    """
    get pascal triangle row
    :param n:
    :return:
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        row = get_row(n - 1)
        return [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]


def pascal_triangle(n):
    """
    pascal triangle
    :param n:
    :return:
    """
    return [get_row(x) for x in range(1, n + 1)]
