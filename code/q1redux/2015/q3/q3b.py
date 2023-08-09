'''
10
'''
from itertools import permutations

configs = list(permutations("AABCCBDD"))
configs = list(set(configs))

configs.sort()


for i in range(len(configs)):
    print(i+1,''.join(configs[i]))