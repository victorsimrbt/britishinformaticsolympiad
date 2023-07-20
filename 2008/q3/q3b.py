import numpy as np
import itertools
target = [1,2,3,4,5,6,7]

def op1(shirts):
    removed_shirt = shirts[0]
    new_shirts = shirts[1:]
    new_shirts.insert(3,removed_shirt)
    return new_shirts

def op2(shirts):
    removed_shirt = shirts[-1]
    new_shirts = shirts[:-1]
    new_shirts.insert(3,removed_shirt)
    return new_shirts

def op3(shirts):
    removed_shirt = shirts[3]
    new_shirts = shirts[:3]+shirts[4:]
    new_shirts.insert(0,removed_shirt)
    return new_shirts

def op4(shirts):
    removed_shirt = shirts[3]
    new_shirts = shirts[:3]+shirts[4:]
    new_shirts.append(removed_shirt)
    return new_shirts

operations = [op1,op2,op3,op4]

permutation = list(itertools.product(operations, repeat=2))
print(len(permutation))
possibilities = []

count = 0
for perm in permutation:
    result = [1,2,3,4,5,6]
    for operation in perm:
        result = operation(result)
    if ''.join([str(val) for val in result]) not in possibilities:
        count += 1
        possibilities.append(''.join([str(val) for val in result]))
print(len(possibilities))


