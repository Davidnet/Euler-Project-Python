def productlist(l):
    p = 1
    for j in l:
        p *= j
    return p


l = list(range(1, 21))
bound = productlist(l)
candidates = []
flag = True


def procedures():
    for i in range(1, bound):
        x = []
        x = [i % f for f in l]
        if sum(x) == 0:
            if flag:
                candidates.append(i)
                return candidates
                flag = False

print(procedures())
