from math import sqrt
L = 1000


def p_trip(ps):
    for m in range(int(sqrt(ps/2)), int(sqrt(ps)/2), -1):
        n = ps / (2*m) - m
        if n > 0 and n % 1 == 0:
            a, b, c = m*m - n*n, 2*m*n, m*m + n*n
            return map(int, (a, b, c, a*b*c))

a, b, c, p = p_trip(L)
print(a, '+', b, '+', c, '=', L, 'product abc =', p)
