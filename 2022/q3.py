import string
import numpy as np
letters = string.ascii_lowercase
config,idx = input().split()
idx = int(idx)-1

config_possibilities = {}

for i in range(len(config)):
    car = config[i]
    possibilities = [letters[i]]
    previous_cars = config[:i]
    #print(car,possibilities,previous_cars)
    for prev_car in range(len(previous_cars)-1,-1,-1):
        if previous_cars[prev_car] < car:
            possibilities.append(letters[prev_car])
        else:
            break
    config_possibilities[car] = possibilities

for key in sorted(config_possibilities):
    config_possibilities[key] = sorted(config_possibilities[key])

clean_config = {}

for key in sorted(config_possibilities):
    clean_config[key] = sorted(config_possibilities[key])
    
ans = []
options = np.prod([len(config_possibilities[key]) for key in config_possibilities])
for key in reversed(sorted(config_possibilities)):
    #print(key,config_possibilities[key],idx)
    ans.append(config_possibilities[key][idx % len(config_possibilities[key])].upper())
    idx = idx // len(config_possibilities[key])
print(''.join(list(reversed(ans))))