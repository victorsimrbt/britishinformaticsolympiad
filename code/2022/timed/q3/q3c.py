'''
ABC

ABCDEFGHIJKLMNOP

ABCDEFGHIJKLMNOP

ADEFGHIJKLMNOPBC

the first preference list must be each car getting their preferred choice
there is only spot with two possibilities
only one letter before that spot which is smaller than it


where all the letters before it are later apart from 1
1

exactly one character has a character before it which is smaller
'''

import string
import itertools

# # parking,target = input().split()
# parking = input()
# # target = int(target) - 1
# alphabet = sorted(parking)
# big_alpha = string.ascii_uppercase
# num_configs = 1

# possibilities = []

# # ! iterate through letters and build possiblities

# for letter in alphabet:
#     options = []
#     for i in range(len(parking)):
#         if parking[i] == letter:
#             options.append(i)
#             break
#         if parking[i] < letter:
#             options.append(i)
#         else:
#             options = []
#     # print(letter,options)
#     num_configs *= len(options)
# print(num_configs)

for parking in itertools.permutations("abcd"):
    alphabet = sorted(parking)
    big_alpha = string.ascii_uppercase
    num_configs = 1

    possibilities = []

    # ! iterate through letters and build possiblities
    print(parking)
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
    # print(num_configs)
    print()
    if num_configs == 2:
        print(parking)
        
total = 0
for i in range(1,15+1):
    total += i
print(total)
    


