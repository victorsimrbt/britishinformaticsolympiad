import copy
def move(stacks,stack_1,stack_2):
    # move from stack_1 to stack_2
    if stacks[stack_1] and len(stacks[stack_2]) < 4:
        top_ball = stacks[stack_1].pop()
        stacks[stack_2].append(top_ball)
    return stacks

def state2str(stacks):
    string = ''
    for stack in stacks:
        if stack:
            string += ''.join([str(char) for char in stack])
        else:
            string += "0"
        string += " "
    return string[:-1]

def str2state(string):
    stacks = []
    for stack in string.split():
        if stack == "0":
            stacks.append([])
        else:
            stacks.append([char for char in stack])
    return stacks

def generate_neighbors(stacks):
    neighbors = []
    for stack_1 in range(4):
        for stack_2 in range(4):
            if stack_1 != stack_2:
                neighbor = move(copy.deepcopy(stacks),stack_1,stack_2)
                neighbor_string = state2str(neighbor)
                if not neighbor_string in visited:
                    neighbors.append(neighbor)
						
    return neighbors

dist = {}

root = input()
target = input()

root = str2state(root)
queue = [root]
level = 0
head = 0

visited = set()

while head < len(queue):
    neighbors = []
    for u in queue:
        u_string = state2str(u)
        visited.add(u_string)
        if u_string == target:
            print(level)
            exit()
        neighbors += generate_neighbors(u)
        queue = neighbors
    level += 1


    # last_string = state2str(last)
    # neighbors = generate_neighbors(last)
    # head += 1
    # for neighbor in neighbors:
    #     # string = state2str(neighbor)
    #     if not(string in dist):
    #         dist[string] = dist[last_string] + 1
    #         queue.append(neighbor)
    #     if string == target:
    #         print(dist[string])
    #         exit()