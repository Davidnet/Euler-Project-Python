from functools import reduce


def gcd(a, b):
    """Return the greatest common multipler of two numbers"""
    while b != 0:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    """Return the lowest common multipler of two numbers"""
    return a*b / gcd(a, b)


def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)


print(lcmm(*range(1, 20)))
