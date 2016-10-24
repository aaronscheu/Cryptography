# euclid.py
# python version 2.7.12
# created at 14.10.2016


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


def x_gcd(a, b):
    """Extended Euclidean algorithm as in ax + by = g = gcd(a, b)

    Args:
        a (long): First input value
        b (long): Second input value

    Returns:
        a: greatest common divisor
        x0: multiplier of a
        y0: multiplier of b
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

