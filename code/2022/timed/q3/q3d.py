'''
The final arrangement for 16 cars is abcdefghijklmnop and exactly 3 cars are in their preferred
position. How many potential preference lists are there?

car a must be in its preferred position

a car will end up in the spot if all spaces before it are filled

a car's preferred position can be any of the positions before it
012

the cars in preferred positions:

1 must be a
the other two are arbitrary

'''
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
    possibilities.append(options)
print(num_configs)

ans = 0 
for idx_1 in range(1,16):
    for idx_2 in range(idx_1+1,16):
        num_pos = 1
        for i in range(1,len(possibilities)):
            if i != idx_1 and i != idx_2:
                num_pos *= (len(possibilities[i])-1)
        ans += num_pos
print(ans)