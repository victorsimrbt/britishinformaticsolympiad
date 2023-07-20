'''
a car's possible preferred spot is the spot it is currently in and all the consecutive occupied spots that come before it

preferred spot is: current spot + consecutive spots that are smaller than it

decide which "bin" it belongs in

given number of options and target_idx, divide target by options to see options per choice
find bin that contains choice
find excess target and repeat
'''
import string
ans = ''
    
parking,target = input().split()
target = int(target) - 1
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
    num_configs *= len(options)
    possibilities.append(options)
    # print(letter,options)
    
for i in range(len(possibilities)):
    # print(possibilities[i])
    configs_per_option = num_configs/len(possibilities[i])
    option = target // configs_per_option
    target -= configs_per_option * option
    # print(target,option,configs_per_option)
    ans += big_alpha[possibilities[i][int(option)]]
    num_configs /= len(possibilities[i])
print(ans)
    