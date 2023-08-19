'''
16
'''
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
    if grid[(r,c)] == 4:
        update.append((r,c))
        
def update_grid(grid):
    while update:
        for square in update:
            r,c = square
            adjacent = adj(r,c)
            grid[(r,c)] = 0
            update.remove((r,c))
            for point in adjacent:
                adj_r,adj_c = point
                if (adj_r,adj_c) in grid:
                    grid[(adj_r,adj_c)] += 1
                else:
                    grid[(adj_r,adj_c)] = 1
                # print()
                if grid[(adj_r,adj_c)] == 4:
                    update.append((adj_r,adj_c))
            print(update)
    return grid
    
grid = {}
for i in range(1,26):
    r,c = num2coord(i)
    # print(r,c)
    grid[(r,c)] = 0
    # print(adj(r,c))


place(3,grid)
place(3,grid)
place(3,grid)
place(3,grid)

update_grid(grid)
print_grid(grid)
print(grid)
print()

place(3,grid)
place(3,grid)
place(3,grid)
place(3,grid)

update_grid(grid)
print_grid(grid)
print(grid)
print()

place(3,grid)
place(3,grid)
place(3,grid)
place(3,grid)

update_grid(grid)
print_grid(grid)
print(grid)
print()

place(3,grid)
place(3,grid)
place(3,grid)
place(3,grid)

update_grid(grid)
print_grid(grid)
print(grid)
print()

# update_grid(grid)
# print_grid(grid)
# # grid = {}
    
    
