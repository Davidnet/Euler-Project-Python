def nthtrianglenum(n):
    return (n * (n + 1)) / 2


def numberofdivisors(n):
    divisors = 1
    count = 0
    f = 2
    while n % f == 0:
        count += 1
        n /= f
    divisors *= (count + 1)
    f = 3
    while f <= n:
        counter = 0
        while n % f == 0:
            counter += 1
            n /= f
        divisors *= (counter + 1)
        f += 2
    return divisors


def unique_divisors(n):
    if n % 2 == 0:
        n /= 2
    return numberofdivisors(n)


def first_triangle_with_more_than_n_divisor(n):
    i = 1
    f1 = unique_divisors(n)
    f2 = unique_divisors(n + 1)
    while f1 * f2 <= n:
        f1 = f2
        f2 = unique_divisors(i + 2)
        i += 1
    return i

n = 500
res = first_triangle_with_more_than_n_divisor(n)

print(res)
