import itertools
import numpy as np 
from math import comb

numbers = list(range(1,11)) * 4

possibilities = itertools.combinations(numbers,5)

works = []
sum_15 = 0
for possibility in possibilities:
    if sum(possibility) == 15:
        if not(sorted(possibility)) in works:
            works.append(sorted(possibility))
        sum_15 += 1

print(len(works))