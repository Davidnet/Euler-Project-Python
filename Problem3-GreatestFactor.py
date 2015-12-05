import math
factor = []

for i in range(int(math.sqrt(600851475143))):
    if i != 0:
        if 600851475143 % i  == 0:
            factor.append(i)

print(factor)
