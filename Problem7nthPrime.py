candidates = list(range(116684))

for i in candidates:
    if i == 0:
        candidates.remove(0)
    if i == 1:
        candidates.remove(1)
    if i != 1 and i != 0:
        ithmultiples = set(range(2*i, 116684, i))
        candidates = [x for x in candidates if x not in ithmultiples]

print(len(candidates))
print(candidates[10001])
print(candidates[10001])
"""11017
104743
104743
[Finished in 114.648s]"""
