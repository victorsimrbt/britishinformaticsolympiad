'''
41049
'''
import math
memo = {}
def isprime(n):
    if n in memo:
        return memo[n]
    else:
        for f in range(2,int(math.sqrt(n))+1):
            if n % f == 0:
                memo[n] = False
                return memo[n]
        memo[n] = True
    return memo[n]

def gen_neighbor(num,l):
    power = 0
    neighbors = []
    
    power = 0
    while True:
        neighbor = num + pow(2,power)
        if neighbor > l:
            break
        if isprime(neighbor):
            neighbors.append(neighbor)
            # dist[neighbor] = distance + 1
        power += 1
    return neighbors

pairs = set()
for i in range(2,250000):
    if isprime(i):
        neighbors = gen_neighbor(i,250000)
        for neighbor in neighbors:
            pairs.add(tuple(sorted([i,neighbor])))
# print(pairs)
print(len(pairs))