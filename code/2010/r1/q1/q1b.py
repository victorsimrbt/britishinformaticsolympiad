from itertools import permutations


number = list("85247910")
permutations = list(permutations(number))
print(permutations)
valid = [''.join(permutation) for permutation in permutations if 85247910 % int(''.join(permutation)) == 0]
print(valid)