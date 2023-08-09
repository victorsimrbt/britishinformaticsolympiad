'''
bottom left is (0,0)
ships are placed assuming  that the right most square is the coordinate
'''
import numpy as np
# ! first is x, second is y

grid = [["O"]*10 for i in range(10)]
# print(grid[9])

# grid[0][0] = "X"
# grid[0][1] = "X"

def print_grid(grid):
    for y in range(9,-1,-1):
        row = ''
        for x in range(10):
            row += str(grid[x][y])
        print(row)
        
def adj(x,y):
    '''
    \ | /
    - O -
    / | \
    '''
    adjacent = [
        [x,y+1],
        [x+1,y+1],
        [x+1,y],
        [x+1,y-1],
        [x,y-1],
        [x-1,y-1],
        [x-1,y],
        [x-1,y+1],
    ]
    valid = [pt for pt in adjacent if pt[0] >= 0 and pt[0] < 10 and pt[1] >= 0 and pt[1] < 10]
    return valid

orienttoinc = {
    "H" : (1,0),
    "V" : (0,1)
}
        
def place(length,coord,orient):
    inc = orienttoinc[orient]
    ship_pts = [coord + np.array(inc)*i for i in range(length)]
    for pt in ship_pts:
        x,y = pt
        if x >= 0 and x < 10 and y >= 0 and y < 10  and grid[x][y] == "O":
            adjacent = adj(x,y)
            for adj_point in adjacent:
                if not(grid[adj_point[0]][adj_point[1]] == "O"):
                    return False
        else:
            return False
    return ship_pts


a,c,m = map(int,input().split())
r = 0
ships = [4,3,3,2,2,2,1,1,1,1]

for ship_len in ships:
    while True:
        r = (a*r+c) % m
        ones = int(str(r)[-1])
        if len(str(r)) == 1:
            tens = 0
        else:
            tens = int(str(r)[-2])
        x,y = ones,tens
        r = (a*r+c) % m
        if r % 2 == 0:
            pts = place(ship_len,[x,y],"H")
            print_txt = "{} {} {}".format(x,y,"H")
        else:
            pts = place(ship_len,[x,y],"V")
            print_txt = "{} {} {}".format(x,y,"V")
        if pts:
            for point in pts:
                x,y = point
                grid[x][y] = "X"
            print(print_txt)
            break
            
# pts = place(1,[0,0],"H")
# if pts:
#     for point in pts:
#         x,y = point
#         grid[x][y] = "X"

# for x in range(10):
#     for y in range(10):
        
#         print((x,y),adj(x,y))
# print_grid(grid)

