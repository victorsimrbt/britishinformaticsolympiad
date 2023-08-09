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
    return [option for option in options if abs(len(option)-len(string)) <= 5 and is_neighbour(string,option)]

queue = []
visited = []

def bfs(node,target):
    node = num2string(node)
    target = num2string(target)
    queue = [[node,1]]
    end = False
    visited = set()
    head = 0
    while head < len(queue):
        string = queue[head][0]
        distance = queue[head][1]
        head += 1
        
        neighbours = generate_neighbours(string)
        #print(neighbours)
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append([neighbour,distance+1])
                visited.add(neighbour)
            if neighbour == target:
                print(distance)
                end = True
                break
            
        if end == True:
            break
    # print(queue)
params = []
for i in range(3):
    params.append([int(value) for value in input().split()])

for param in params:
    bfs(param[0],param[1])

