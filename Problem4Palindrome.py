import math

def isPerfectSquare(n):
    return n==int(math.sqrt(n))**2

def is_num_palindrome(n):
    numstr = str(n)
    if numstr == (numstr[::-1]):
        return True
    else:
        return False

candidates = []
for i in range(100,999):
    for j in range (100,999):
        test = i*j
        if is_num_palindrome(test):
            candidates.append(test)
print(max(candidates))
