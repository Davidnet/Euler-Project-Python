import math


def isPrime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

limit = 10001
count = 1
candidate = 1
while not count == limit:
    candidate += 2
    if isPrime(candidate):
        count += 1

print(candidate)


print(isPrime(7913))
