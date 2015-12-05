def Sumdivisibleby(n,total):
    ''' Given a number, return the sum of all numbers that are divisible by n'''
    sum = 0
    for x in range(0,total):
        if x % n == 0:
            sum = sum + x
    return sum


for x in range(0,1000):
    sol = Sumdivisibleby(3,1000) + Sumdivisibleby(5,1000) - Sumdivisibleby(15,1000)
print(sol)
