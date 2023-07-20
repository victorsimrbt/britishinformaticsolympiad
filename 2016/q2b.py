
people = {}
overcrowded = []
# p,s,n = [int(char) for char in input().split()]
# # p,s,n = 8,1,6
# seq = [int(char) for char in input().split()]

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
    
add_person(num2pos(15))
add_person(num2pos(15))
add_person(num2pos(15))
add_person(num2pos(15))

head = 0
while head < len(overcrowded):
    coord = overcrowded[head]
    adj = neighbors(coord)
    for square in adj:
        add_person(square)
    people[tuple(coord)] = people[tuple(coord)] % 4
    head += 1

add_person(num2pos(15))
add_person(num2pos(15))
add_person(num2pos(15))
add_person(num2pos(15))

head = 0
while head < len(overcrowded):
    coord = overcrowded[head]
    adj = neighbors(coord)
    for square in adj:
        add_person(square)
    people[tuple(coord)] = people[tuple(coord)] % 4
    head += 1
    
add_person(num2pos(15))
add_person(num2pos(15))
add_person(num2pos(15))
add_person(num2pos(15))

head = 0
while head < len(overcrowded):
    coord = overcrowded[head]
    adj = neighbors(coord)
    for square in adj:
        add_person(square)
    people[tuple(coord)] = people[tuple(coord)] % 4
    head += 1

add_person(num2pos(10))
add_person(num2pos(10))

head = 0
while head < len(overcrowded):
    coord = overcrowded[head]
    adj = neighbors(coord)
    for square in adj:
        add_person(square)
    people[tuple(coord)] = people[tuple(coord)] % 4
    head += 1


print_solution()

[1,3,6,8,11,16,18,21]

p = 3
s = [2,3,2]
[2,3,2,3,5,3,2]