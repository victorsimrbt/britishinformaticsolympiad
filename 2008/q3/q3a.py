import numpy as np
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

print(op4([1, 2, 3, 4, 5, 6,7]))

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
path = []

def bfs(visited, node):
    visited.append(node)
    #print(node)
    queue.append([node,1])

    while queue:
        s = queue.pop(0)
        new = s[0]
        distance = s[1]
        #print(s[0], end = " ") 
        
        neighbours = []
        for operation in operations:
            neighbours.append(operation(new))
        #print(neighbours)
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append([neighbour,distance + 1])
            if neighbour == target:
                print(distance)
                return

shirts = [int(value) for value in input()]
bfs(visited, shirts)
