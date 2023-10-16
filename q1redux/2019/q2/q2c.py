'''
441
'''
grid = {}
pos = [0,0]
direction = "U"

t,instructions,m = 1000000000,"L",100
t = int(t)
m = int(m)

# ! x y system
U = [0,1]
D = [0,-1]
L = [-1,0]
R = [1,0]

'''
   U
   |
L--|--R
   |
   D
'''

dir_to_vec = {
    "U" : U,
    "D" : D,
    "L" : L,
    "R" : R
}

U_dict = {
    "L" : "L",
    "R" : "R",
    "F" : "U",
    "D" : "D"
}

D_dict = {
    "L" : "R",
    "R" : "L",
    "F" : "D",
    "D" : "U"
}

L_dict = {
    "L" : "D",
    "R" : "U",
    "F" : "L",
    "D" : "R"
}

R_dict = {
    "L" : "U",
    "R" : "D",
    "F" : "R",
    "D" : "L"
}

order = ["F","R","D","L"]

def print_grid(i,pos):
    for y in range(6,-6,-1):
        row = ''
        for x in range(-6,6):
            if (x,y) == tuple(pos):
                row += "X"
                row += " "
                continue
            if (x,y) in grid:
                if i+1 - grid[(x,y)]+1 <= t-1:
                    row += str(i+1 - grid[(x,y)]+1)
                else:
                    row += "_"
                # row += str(grid[(x,y)])
            else:
                row += "_"
            row += " "
        print(row)
                
i = 0
while True:
    grid[tuple(pos)] = i+1
    instruction = instructions[i%len(instructions)]
    
    if direction == "U":
        translate = U_dict
    if direction == "D":
        translate = D_dict
    if direction == "L":
        translate = L_dict
    if direction == "R":
        translate = R_dict
        
    idx = order.index(instruction)
    while True:
        direction = translate[order[idx]]
        ahead = pos[:]
        vector = dir_to_vec[direction]
        ahead[0] += vector[0]
        ahead[1] += vector[1]
        if tuple(ahead) in grid and i-grid[tuple(ahead)]+1 <= t-1:
            # print(i+1 - grid[tuple(ahead)])
            idx = (idx + 1) % 4
        else:
            pos = ahead
            break
        
    visited = True
    for x in range(-10,11):
        for y in range(-10,11):
            if (x,y) in grid:
                pass
            else:
                visited = False
    if visited:
        print(i+1)
        exit()
        
    # print(direction)
    # print(grid)
    # print(i)
    # print_grid(i,pos)
    # print()
    i += 1
print(tuple(pos))
    


