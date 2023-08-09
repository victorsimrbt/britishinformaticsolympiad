import numpy as np
distinct_factors = []
def prime_fact(value):
    if value == 1:
        return
    for number in range(2,100000):
        if value % number == 0:
            factors.append(number)
            prime_fact(value/number)
            break

for i in range(1,1000000):
    if i % 1000 == 0:
        values,counts = np.unique(distinct_factors,return_counts = True)
        print(values[np.argmax(counts)],max(counts))
    factors = []
    prime_fact(i)
    distinct_factors.append(np.prod(list(set(factors))))
