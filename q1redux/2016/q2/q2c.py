'''
21 3 8 5 7 23

20 configs
'''
update = []
import time
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
                    grid[(adj_r,adj_c)] = 0
                # print()
                if grid[(adj_r,adj_c)] == 4:
                    update.append((adj_r,adj_c))
            # print(update)
    return grid


# ! starting position (p) between 1 and 25
# ! sequuence size set at 3
# ! n is set at 8
ans = 0
for p in range(1,26):
    p,s,n = p,3,8
    # sequence = [0]
    sequence = []
    for num1 in range(0,25):
        for num2 in range(0,25):
            for num3 in range(0,25):
                sequence = [num1,num2,num3]
        
                grid = {}
                for i in range(1,26):
                    r,c = num2coord(i)
                    # print(r,c)
                    grid[(r,c)] = 0
                    # print(adj(r,c))

                position = p
                for i in range(n):
                    position += sequence[i%len(sequence)]
                    if position > 25:
                        position -= 25
                    place(position,grid)
                    update_grid(grid)
                
                covered = [1,3,6,8,11,16,18,21]
                success = True
                for pt in covered:
                    r,c = num2coord(pt)
                    # print(grid[(r,c)])
                    if grid[(r,c)] == 1:
                        pass
                    else:
                        success = False
                        
                if success == True:
                    print(success)
                    print()
                    print(p,s,n,num1,num2,num3)
                    print()
                    print_grid(grid)
                    ans += 1
                # time.sleep(1)
                # print_grid(grid)
print("ANS",ans)
# place(14,grid)
# place(14,grid)
# place(14,grid)

# place(8,grid)
# place(8,grid)
# place(8,grid)

# place(12,grid)
# place(12,grid)
# place(12,grid)

# place(18,grid)
# place(18,grid)
# place(18,grid)


# place(1,grid)
# place(1,grid)
# place(1,grid)
# place(1,grid)

# update_grid(grid)
# print_grid(grid)

# update_grid(grid)
# print_grid(grid)
# # grid = {}
    
    
