'''
6

ABC
ACB
BAC
BCA
CAB
CBA
'''
from itertools import permutations

print(list(permutations("ABC")))