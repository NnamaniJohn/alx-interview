#!/usr/bin/python3
"""
minimum operation
"""


def minOperations(n: int) -> int:
    """
    minimum operation
    :param n:
    :return:
    """
    if n < 2:
        return 0
    factors = []
    factor = 2
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n /= factor
        else:
            factor += 1

    return sum(factors)
