def collatz_computation(n):
    if n % 2 == 0:
        return n / 2
    return 3*n + 1

candidate = 0
largestchain = 0
for j in range(2, 1000000):
    member = j
    iteration = 0
    while collatz_computation(j) != 1:
        iteration += 1
        j = collatz_computation(j)
    if iteration > largestchain:
        candidate = member
        largestchain = iteration
print(largestchain)
print(candidate)
