
p,s,n = map(int,input().split())
# sequence = [0]
sequence = list(map(int,input().split()))
import time
# for i in range(s):
#     sequence.append(int(input()))
    
update = []
def num2coord(num):
    # ! model top left as 0,0
    num -= 1
    r,c = num // 5, num % 5
    return r,c

def adj(r,c):
    adjacent = [
        [r-1,c],
        [r,c+1],
        [r+1,c],
        [r,c-1]
    ]
    return adjacent

def print_grid(grid):
    for r in range(5):
        row = ''
        for c in range(5):
            row += str(grid[(r,c)]) + ' '
        print(row)

def place(num,grid):
    r,c = num2coord(num)
    grid[(r,c)] += 1
    if grid[(r,c)] >= 4:
        update.append((r,c))
        
def update_grid():
    global grid
    # print(overcrowded)
    # print(update)
    while update:
        coord = update[0]
        adjacent = adj(coord[0],coord[1])
        for square in adjacent:
            if tuple(square) in grid:
                if grid[tuple(square)] >= 4:
                    update.append(square)
            if tuple(square) in grid:
                grid[tuple(square)] += 1
            else:
                grid[tuple(square)] = 1
        grid[tuple(coord)] -= 4
        update.remove(coord)
        # head += 1
        
    
grid = {}
for i in range(1,26):
    r,c = num2coord(i)
    grid[(r,c)] = 0
    
position = p
place(position,grid)
for i in range(n-1):
    position += sequence[i%len(sequence)]
    if position > 25:
        position -= 25
    place(position,grid)
    print_grid(grid)
    print(grid)
    print(update)
    update_grid()
    print_grid(grid)
    print()
    update = []
print_grid(grid)
    
