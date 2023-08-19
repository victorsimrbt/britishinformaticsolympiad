'''
596
'''
import numpy as np
# ! first is x, second is y

grid = [["O"]*10 for i in range(10)]

def print_grid(grid):
    for y in range(4,-1,-1):
        row = ''
        for x in range(5):
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
    valid = [pt for pt in adjacent if pt[0] >= 0 and pt[0] < 5 and pt[1] >= 0 and pt[1] < 5]
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
        if x >= 0 and x < 5 and y >= 0 and y < 5 and grid[x][y] == "O":
            adjacent = adj(x,y)
            for adj_point in adjacent:
                if not(grid[adj_point[0]][adj_point[1]] == "O"):
                    return False
        else:
            return False
    return ship_pts

ships = [4,3,2,1]
ans = 0
repeats = []
for fourx in range(5):
    print(fourx)
    for foury in range(5):
        for fouro in ["H","V"]:
            for threex in range(5):
                for threey in range(5):
                    for threeo in ["H","V"]:
                        for twox in range(5):
                            for twoy in range(5):
                                for twoo in ["H","V"]:
                                    for onex in range(5):
                                        for oney in range(5):
                                            grid = [["O"]*5 for i in range(5)]
                                            pts = place(4,[fourx,foury],fouro)
                                            if pts:
                                                for point in pts:
                                                    x,y = point
                                                    grid[x][y] = "A"
                                                pts = place(3,[threex,threey],threeo)
                                                if pts:
                                                    for point in pts:
                                                        x,y = point
                                                        grid[x][y] = "B"
                                            
                                                    pts = place(2,[twox,twoy],twoo)
                                                    if pts:
                                                        for point in pts:
                                                            x,y = point
                                                            grid[x][y] = "C"
                                            
                                                        pts = place(1,[onex,oney],"H")
                                                        if pts:
                                                            for point in pts:
                                                                x,y = point
                                                                grid[x][y] = "D"
                                                            serialise = ''
                                                            for row in grid:
                                                                serialise += ''.join(row) + " "
                                                            if serialise in repeats:
                                                                print_grid(grid)
                                                            else:
                                                                repeats.append(serialise)
                                                            ans += 1
                                            # print_grid(grid)
                                            # print()
print(ans,len(repeats))
print(serialise)
                                            
# for ship in ships:
        

