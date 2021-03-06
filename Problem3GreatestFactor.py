import math


def factorization(n):
    divisor = []
    bound = int(math.sqrt(n))
    for i in range(bound):
        if i != 0:
            if n % i == 0:
                divisor.append(i)
    return divisor


def prime_factors(n):
    """
    Takes a positive integer, and returns its list of prime divisors
    :rtype: list of prime factors
    """
    divisor = []
    bound = int(math.sqrt(n))
    for i in range(bound):
        if i != 0:
            if n % i == 0:
                divisor.append(i)
    for d in divisor:
        for f in divisor:
            if f != d and f % d == 0 and d != 1:
                divisor.remove(f)
    return divisor

"""
x = prime_factors(600851475143)
print(max(x))
"""
