'''
can different configurations lead to the same final state?
yes
two different states can lead to the same final state
information is lost during the step.
when the 4 disperses, information is lost
Counterexample:
00000
03330
00000

becomes

01110
10201
01110

but 

01110
10101
01110

also becomes


01110
10201
01110
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


place(13,grid)
place(13,grid)
place(13,grid)

place(14,grid)
place(14,grid)
place(14,grid)

place(12,grid)
place(12,grid)
place(12,grid)

place(13,grid)

update_grid(grid)
print_grid(grid)
print(grid)
print()


'''

00000
03330
00000

becomes

01110
10201
01110

but 

01110
10101
01110

also becomes


01110
10201
01110


'''
# update_grid(grid)
# print_grid(grid)
# # grid = {}
    
    
