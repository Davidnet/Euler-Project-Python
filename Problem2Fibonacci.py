def nthFibonacci(num):
    if num == 0:
        return 1
    if num == 1:
        return 2
    else:
        return nthFibonacci(num - 1) + nthFibonacci(num - 2)

sum = 0
flag = False
iter = 0

while flag != True:
    x = nthFibonacci(iter)
    if x <= 4000000:
        iter = iter + 1
        if x % 2 == 0:
            sum = sum + x
    else:
        print(sum)  
        flag = True
