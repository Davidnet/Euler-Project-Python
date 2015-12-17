def nthsum(n):
    """Returns the sum of the first n integer terms"""
    return n*(n+1) / 2


def nthsumsquare(n):
    """Return the sum of the first nth perfect square numbers"""
    return n*(n+1)*(2*n+1) / 6


print(nthsum(100)**2 - nthsumsquare(100))
