from itertools import permutations
from copy import deepcopy

num_jars,target = [int(value) for value in input().split()]
capacity = [int(value) for value in input().split()]

visited = []
queue = [] 

def move(idx_1,idx_2,volume):
    # Move water from jar 1 to jar 2
    water_moved = min(capacity[idx_2] - volume[idx_2],volume[idx_1])
    volume[idx_1] -= water_moved
    volume[idx_2] += water_moved
    return volume
    
def fill(idx,volume):
    volume[idx] = capacity[idx]
    return volume
    
def empty(idx,volume):
    volume[idx] = 0
    return volume
    
def generate_neighbours(volume):
    neighbours = []
    if num_jars > 1:
        move_configs = permutations(list(range(num_jars)))
    else:
        move_configs = []
    fill_configs = list(range(num_jars))
    empty_configs = list(range(num_jars))
    
    for config in move_configs:
        new_volume = move(config[0],config[1],volume[:])
        if new_volume != volume and new_volume not in neighbours:
            neighbours.append(new_volume)
    
    for config in fill_configs:
        new_volume = fill(config,volume[:])
        if new_volume != volume and new_volume not in neighbours:
            neighbours.append(new_volume)
        
    for config in empty_configs:
        new_volume = empty(config,volume[:])
        if new_volume != volume and new_volume not in neighbours:
            neighbours.append(new_volume)
    return neighbours
    
def bfs(visited,node):
    visited.append(node)
    queue.append([node,1])
    
    while queue:
        s = queue.pop(0)
        new = s[0]
        distance = s[1]
        
        neighbours = generate_neighbours(new)
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append([neighbour,distance + 1])
            if target in neighbour:
                print(distance)
                return

bfs(visited,[0]*num_jars)
    
