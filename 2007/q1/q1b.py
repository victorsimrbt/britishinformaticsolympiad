import itertools
import numpy as np 
from math import comb

numbers = list(range(1,11))

possibilities = itertools.combinations(numbers,5)

for possibility in possibilities:
    numbers = possibility
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
    if score+len(combinations) == 0:
        print(numbers)