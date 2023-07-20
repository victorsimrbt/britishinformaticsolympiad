import string
import itertools

# parking,target = input().split()
parking = input()
# target = int(target) - 1
alphabet = sorted(parking)
big_alpha = string.ascii_uppercase
num_configs = 1

possibilities = []

# ! iterate through letters and build possiblities

for letter in alphabet:
    options = []
    for i in range(len(parking)):
        if parking[i] == letter:
            options.append(i)
            break
        if parking[i] < letter:
            options.append(i)
        else:
            options = []
    print(letter,options)
    num_configs *= len(options)
print(num_configs)