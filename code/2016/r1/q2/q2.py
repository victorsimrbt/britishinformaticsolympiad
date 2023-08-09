
people = {}
overcrowded = []
p,s,n = [int(char) for char in input().split()]
# p,s,n = 8,1,6
seq = [int(char) for char in input().split()]

def num2pos(num):
    x = (num-1) % 5
    y = 4-((num-1) // 5)
    return [x,y]

def neighbors(coord):
    x,y = coord
    adjacent = []
    adjacent.append([x,y+1])
    adjacent.append([x+1,y])
    adjacent.append([x,y-1])
    adjacent.append([x-1,y])
    return adjacent

def add_person(coord):
    global overcrowded
    global people
    if tuple(coord) in people:
        people[tuple(coord)] += 1
    else:
        people[tuple(coord)] = 1
    if people[tuple(coord)] == 4:
        overcrowded.append(coord)
        
def print_solution():
    print_string = ''
    for i in range(1,26):
        coord = num2pos(i)
        print_string += str(people[tuple(coord)]) + ' '
        if i % 5 == 0:
            print(print_string)
            print_string = ''

for i in range(1,26):
    people[tuple(num2pos(i))] = 0
    # print(i,num2pos(i),neighbors(num2pos(i)))
    
# add_person([2,1])
# add_person([2,1])
# add_person([2,1])

# add_person([3,1])
# add_person([3,1])
# add_person([3,1])

# add_person([3,2])
# add_person([3,2])
# add_person([3,2])

# add_person([3,1])
# head = 0
# print_solution()
# print()
# while head < len(overcrowded):
#     coord = overcrowded[head]
#     adj = neighbors(coord)
#     for square in adj:
#         add_person(square)
#     people[tuple(coord)] = 0
#     head += 1
# print_solution()
add_person(num2pos(p))
for i in range(n-1):
    p += seq[i % s]
    if p > 25:
        p -= 25
    # print(p)
    add_person(num2pos(p))
    
    head = 0
    while head < len(overcrowded):
        coord = overcrowded[head]
        adj = neighbors(coord)
        for square in adj:
            add_person(square)
        people[tuple(coord)] = people[tuple(coord)] % 4
        head += 1
        # print_solution()
        # print("YAH")
    
    overcrowded = []
    # print_solution()
    # print()
print_solution()

'''
represent people as dictionary

people = {}
overcrowded = []
p,s,n = [int(char) for char in input().split()]
mod = [s,n]

def num2pos(num):
    x = (num % 5)-1)
    y = 4-num // 5
    return [x,y]

def neighbors(coord):
    x,y = coord
    adjacent = []
    adjacent.append([x,y+1])
    adjacent.append([x+1,y])
    adjacent.append([x,y-1])
    adjacent.append([x-1,y])
    return adjacent
    
def add_person(coord):
    global overcrowded
    if tuple(coord) in people:
        people[tuple(coord)] += 1
    else:
        people[tuple(coord)] = 1
    if people[tuple(coord)] == 4:
        overcrowded.append(square)

def print_solution():
    print_string = ''
    for i in range(1,26):
        coord = num2pos(i)
        print_string += people[coord]
        if i % 5 == 0:
            print(print_string)
            print_string = ''
        

add_person(num2pos(p))
for i in range(n):
    p += mod[i % 2]
    add_person(num2pos(p))
    head = 0
    while head < len(overcrowded):
        coord = overcrowded[head]
        adj = neighbors(coord) + [coord]
        for square in adj:
            add_person(square)
        head += 1
    overcrowded = []
print_solution()
'''