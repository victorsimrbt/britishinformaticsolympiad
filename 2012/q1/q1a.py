import numpy as np
factors = []
def prime_fact(value):
    if value == 1:
        return
    for number in range(2,100000):
        if value % number == 0:
            factors.append(number)
            prime_fact(value/number)
            break

prime_fact(int(input()))
print(factors)
print(np.prod(list(set(factors))))