def adj(row,column):
    adj = [
        [row-1,column],
        [row,column+1],
        [row+1,column],
        [row,column-1]
    ]
    valid = []
    for point in adj:
        row,column = point
        if row >=0 and row <= 3 and column >= 0 and column <= 3:
            valid.append(tuple(point))
    return valid

def find_block(row,column):
    visited = set()
    queue = [(row,column,1,[(row,column)])]
    visited.add((row,column))
    head = 0
    max_size = 0
    max_path = None
    while head < len(queue):
        row,column,size,path = queue[head]
        adjacent = adj(row,column)
        for point in adjacent:
            if not(point in visited) and grid[point[0]][point[1]] == grid[row][column] and not point in path:
                visited.add(point)
                queue.append((point[0],point[1],size+1,path+[point]))
                if size+1 > max_size:
                    max_path = path+[point]
                    max_size = size + 1
        head += 1
    # print(queue)
    if len(visited) > 1:
        # print("WHAT",visited)
        return len(visited),list(visited)
    else:
        return 0,0

def play_move(grid):
    covered = set()
    score = 1
    for r in range(4):
        for c in range(4):
            if not (r,c) in covered:
                # print("ADJACNET",(r,c),adj(r,c))
            # print()
                block_size,path = find_block(r,c)
                if path and block_size > 1:
                    for point in path:
                        covered.add(point)
                        grid[point[0]][point[1]] = " "
                    score *= block_size
                # print(block_size,path)
    if score == 1:
        # print("YEAH")
        return 0,grid
    else:
        return score,grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))
        
def fix_grid(grid):
    new_grid = [row[:] for row in grid]
    for c in range(4):
        column = [grid[r][c] for r in range(len(grid)) if grid[r][c] != " "]
        while len(column) < 4:
            column.insert(0," ")
        # column = sorted(column)
        # print(column)
        for r in range(4):
            new_grid[r][c] = column[r]
    return new_grid

def drop_pieces(grid):
    # ! drop with first value !!!
    new_grid = [[] for i in range(4)]
    for c in range(4):
        column = [grid[r][c] for r in range(len(grid))]
        for cell in reversed(range(len(column))):
            if column[cell] == " ":
                column[cell] = drop[c].pop(0)
        # print(column)
        for r in range(4):
            new_grid[r].append(column[r])
    return new_grid
    
    
    
grid = [[] for i in range(4)]


for i in range(4):
    grid[i] = list(input())
    
# ! drop with the top facing down
drop = [0 for i in range(4)]
for c in range(4):
    column = list(reversed([grid[r][c] for r in range(len(grid))]))
    drop[c] = column * 100
# print(drop)

score = 0
while True:
    n = int(input())
    if n == 0:
        exit()
    for i in range(n):
        round_score,grid = play_move(grid)
        # print_grid(grid)
        # print()
        grid = fix_grid(grid)
        # print_grid(grid)
        # print()
        grid = drop_pieces(grid)
        
        score += round_score
        if round_score == 0:
            print("GAME OVER")
            print(score)
            exit()
    print_grid(grid)
    print(score)

play_move()
print_grid(grid)

# print("FIXED",fix_grid())
print()

print_grid(fix_grid())
print()
print_grid(drop_pieces(fix_grid()))
# print_grid(grid)
    
