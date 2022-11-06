import numpy as np
digits = ["ZERO","ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

unique = ''
for digit in digits:
    unique += digit
unique = set(unique)

def num2string(num):
    return ''.join([digits[int(instance)] for instance in str(num)])

options = [num2string(i) for i in range(1,1000)]

def is_neighbour(string_1,string_2):
    operations = []
    all_values = set(string_1+string_2)
    for value in all_values:
        operations.append(abs(string_1.count(value)-string_2.count(value)))
    return [True if sum(operations) <= 5 else False][0]

def generate_neighbours(string):
    return [option for option in options if is_neighbour(string,option)]

queue = []
visited = []

def bfs(node,target):
    node = num2string(node)
    target = num2string(target)
    queue = [[node,1]]
    end = False
    for val in queue:
        string = val[0]
        distance = val[1]
        
        neighbours = generate_neighbours(string)
        for neighbour in neighbours:
            if neighbour not in visited and len(neighbour) == len(target):
                queue.append([neighbour,distance+1])
            if neighbour == target:
                print(distance)
                end = True
                break
            
        if end == True:
            break

params = []
for i in range(3):
    params.append([int(value) for value in input().split()])

for param in params:
    bfs(param[0],param[1])

