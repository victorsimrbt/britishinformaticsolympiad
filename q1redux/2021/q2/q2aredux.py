grid = {}
import copy
import time
'''
traverse(edge):
1. Move one edge clockwise on the inside triangle
2. If edge unoccupied, return edge
3. otherwise, set inside triangle to outside triangle and outside triangle to the inside triangle
4. repeat steps 1 to 4 until termination
'''
def traverse(edge):
    in_tri,out_tri = edge
    while True:
        in_tri_edges = get_edges(in_tri)
        # print(in_tri,out_tri,in_tri_edges)
        assert out_tri in in_tri_edges
        start_edge_idx = in_tri_edges.index(out_tri)
        assert len(in_tri_edges) == 3
        # assert out_tri in in_tri_edges
        for inc in range(1,3):
            # ! iterate through edges
            next_edge_idx = (start_edge_idx + inc) % 3
            next_edge = in_tri_edges[next_edge_idx]
            if tuple(next_edge) in grid:
                # print("OCCUPIED")
                # ! if edge is occupied
                # print(in_tri,out_tri)
                in_tri,out_tri = next_edge,in_tri
                break
            else:
                # ! edge is unoccupied
                return in_tri,next_edge
'''
get_edges(triangle):
1. returns edges in clockwise order
2. dependent on whether triangle is up or down
'''

def get_edges(triangle):
    direction = get_direction(triangle)
    x,y = triangle
    if direction == "U":
        '''
         /\
        /__\
        left,right,down
        '''
        left = [x-1,y]
        right = [x+1,y]
        down = [x,y-1]
        return [left,right,down]
    if direction == "D":
        '''
         \''/
          \/
        left,up,right
        '''
        left = [x-1,y]
        up = [x,y+1]
        right = [x+1,y]
        return [left,up,right]

'''
get_direction():
1. returns "U" or "D" for each coordinate
'''

def get_direction(triangle):
    x,y = triangle
    if (x+y) % 2 == 0:
        return "U"
    else:
        return "D"

def second_elem(a):
    return a[1]
def print_grid(grid):
    minx = sorted(grid.keys())[0][0]
    maxx = sorted(grid.keys())[-1][0]
    
    miny = sorted(grid.keys(),key=second_elem)[0][1]
    maxy = sorted(grid.keys(),key=second_elem)[-1][1]
    
    for x in range(minx,maxx):
        row = ''
        for y in range(miny,maxy):
            direction = get_direction([x,y])
            if direction == "U":
                string = " / \ "
            else:
                string = " \ / "
            if (x,y) in grid:
                if direction == "U":
                    string = " /{}\ "
                else:
                    string = " \{}/ "
                string = string.format(grid[(x,y)])
            row += string[1:-1]
        print(row)
                
'''
play(player,traversals):
check if player is in occupied position
1. calls traverse function  *traversals* number of times
2. stops if on edge that completes triangle
3. sets original edge to be occupied by player
'''
def play(player,traversals):
    in_tri,out_tri = map(tuple,positions[player])
    if in_tri in grid and out_tri in grid:
        # ! in occupied
        highest_row = 0
        for key in grid.keys():
            highest_row = max(highest_row,key[1])
            # print("HIGH",highest_row)
        min_row = 0
        for key in grid.keys():
            if key[1] == highest_row:
                min_row = min(min_row,key[0])
        # leftmost = sorted(grid.keys())[0]
        # in_tri = list(leftmost)
        # out_tri = [leftmost[0]-1,leftmost[1]]
        in_tri = [min_row,highest_row]
        out_tri = [min_row-1,highest_row]
        positions[player] = [in_tri,out_tri]
        # print("REPOSITIONED",positions[player])
    start_position = copy.deepcopy(positions[player])
    marker = player+1
    for i in range(traversals):
        positions[player] = traverse(positions[player])
        print(positions[player])
        # print()
        in_tri,out_tri = positions[player]
        if completes_tri(out_tri,marker):
            # print("COMPLETES TRI")
            break
    start_in,start_out = start_position
    start_out = tuple(start_out)
    grid[start_out] = marker
    
'''
completes_tri(out_tri):
1. if triangle is up
'''

def completes_tri(triangle,player):
    x,y = triangle
    assert tuple(triangle) not in grid
    if get_direction(triangle) == "U":
        '''
         /\
        /\/\
        '''
        # ! bottom left case
        right = (x+2,y)
        top = (x+1,y+1)
        if right in grid and top in grid and grid[right] == player and grid[top] == player:
            return True
        
        # ! bottom right case
        left = (x-2,y)
        top = (x-1,y+1)
        if left in grid and top in grid and grid[left] == player and grid[top] == player:
            return True
        
        # ! top tri case
        left = (x-1,y-1)
        right = (x+1,y-1)
        if left in grid and right in grid and grid[right] == player and grid[left] == player:
            return True
    else:
        '''
        \/\/
         \/
        '''
        # ! top left case
        right = (x+2,y)
        bottom = (x+1,y-1)
        if right in grid and bottom in grid and grid[right] == player and grid[bottom] == player:
            return True
        
        # ! top right case
        left = (x-2,y)
        bottom = (x-1,y-1)
        if left in grid and bottom in grid and grid[left] == player and grid[bottom] == player:
            return True
        
        # ! bottom tri case
        left = (x-1,y+1)
        right = (x+1,y+1)
        if left in grid and right in grid and grid[right] == player and grid[left] == player:
            return True
    return False

'''
count_score()
'''
def count_score(triangle,player):
    x,y = triangle
    if get_direction(triangle) == "U":
        '''
         /\
        /\/\
        '''
        # ! bottom left case
        right = (x+2,y)
        top = (x+1,y+1)
        if right in grid and top in grid and grid[right] == player and grid[top] == player:
            return [triangle,right,top]
        
        # ! bottom right case
        left = (x-2,y)
        top = (x-1,y+1)
        if left in grid and top in grid and grid[left] == player and grid[top] == player:
            return [triangle,left,top]
        
        # ! top tri case
        left = (x-1,y-1)
        right = (x+1,y-1)
        if left in grid and right in grid and grid[right] == player and grid[left] == player:
            return [triangle,left,right]
    else:
        '''
        \/\/
         \/
        '''
        # ! top left case
        right = (x+2,y)
        bottom = (x+1,y-1)
        if right in grid and bottom in grid and grid[right] == player and grid[bottom] == player:
            return [triangle,bottom,right]
        
        # ! top right case
        left = (x-2,y)
        bottom = (x-1,y-1)
        if left in grid and bottom in grid and grid[left] == player and grid[bottom] == player:
            return [triangle,left,bottom]
        
        # ! bottom tri case
        left = (x-1,y+1)
        right = (x+1,y+1)
        if left in grid and right in grid and grid[left] == player and grid[right] == player:
            return [triangle,left,right]
    return []

p,m = map(int,input().split())
traversals = list(map(int,input().split()))
positions = [[[0,0],[-1,0]] for i in range(p)]
scores = [0 for i in range(p)]
grid[(0,0)] = 0

for i in range(m):
    player = i % p
    # print(player)
    play(player,traversals[player])
    # print(grid)
    # print(positions)
    print()
    
visited = []
for coord in grid.keys():
    for player in range(p):
        # print(coord)
        big_tri = count_score(coord,player+1)
        if big_tri:
            big_tri = sorted(big_tri)
            if not(big_tri) in visited:
                visited.append(big_tri)
                scores[player] += 1
# print(visited)
for item in scores:
    print(item)

leftmost = sorted(grid.keys())[0]
in_tri = list(leftmost)
out_tri = [leftmost[0]-1,leftmost[1]]
perimeter = 1
edge = [in_tri,out_tri]
left_edge = copy.deepcopy(edge)

while True:
    edge = traverse(edge)
    # print(edge)
    if edge == tuple(left_edge):
        break
    perimeter += 1
    # time.sleep(1)
print(perimeter)

# print_grid(grid)



        
        
    
    