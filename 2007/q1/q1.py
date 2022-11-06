import numpy as np
from math import comb
import itertools

numbers = [int(instance) for instance in input().split()]
        
def identical_score(numbers):
    score = 0
    _,counts = np.unique(numbers,return_counts =True)
    for instance in counts:
        score += comb(instance,2)
    return score

combinations = []
for i in range(6):
    combos = list(itertools.combinations(numbers,i))
    combinations += [combo for combo in combos if sum(combo) == 15]
    
score = identical_score(numbers)
print(score+len(combinations))