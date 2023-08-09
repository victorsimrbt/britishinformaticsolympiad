from itertools import permutations

permus = sorted(set([''.join(item) for item in list(permutations("AABBCCDD"))]))
print(set(permus))
print(permus.index("AABBCCDD"))
print(permus)