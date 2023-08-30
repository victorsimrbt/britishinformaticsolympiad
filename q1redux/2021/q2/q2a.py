'''
each triangle is a coordinate
each edge is described by 4 numbers, triangle 1 and triangle 2
seems like traversing edges clockwise works for all cases
will test

notes:
better-named variables
plan code beforehand
'''
import time
grid = {}
def get_direction(coord):
    if (abs(coord[0]) + abs(coord[1])) % 2 == 0:
        return "U"
    else:
        return "D"

def get_edges(coord):
    # ! clockwise
    x,y = coord
    direction = get_direction(coord)
    if direction == "U":
        edges = [
            [x-1,y],
            [x+1,y],
            [x,y-1]
        ]
    elif direction == "D":
        edges = [
            [x-1,y],
            [x,y+1],
            [x+1,y]
        ]
    return edges
    
def next_edge(edge):
    # print("GETTING",edge)
    # ! assumes that edge is on perimeter (wrong assumption )
    
    tri1,tri2 = edge
    tri1,tri2 = list(tri1),list(tri2)
    tri1_edges = get_edges(tri1)
    while tri1_edges[0] != tri2:
        tri1_edges.append(tri1_edges.pop(0))
        # print("Etri1_edges)
    # print(tri1_edges)
    # print("EDGES",tri1_edges)
    for tri_edge in tri1_edges[1:]:
        # ! check if edge occupied
        if tuple(tri_edge) in grid:
            # print("OCCUPIED",tri_edge)
            # ! is occupied
            # ! if it is occupied, keep getting new edge until u get a valid one
            new_triangle = tri_edge
            new_triangle_edges = get_edges(new_triangle)
            start_edge = new_triangle_edges.index(tri1)
            # print(new_triangle_edges,start_edge)
            next_val = new_triangle_edges[(start_edge + 1) % 3]
            break
            # if next_val in
            # return [tri_edge,new_triangle_edges[next_val]]
        else:
            return [tri1,tri_edge]
    
    if tuple(next_val) in grid:
        return next_edge((next_val,tri_edge))
    else:
        return [tri_edge,next_val]

def forms_triangle(coord,player):
    '''
     /\
    /\/\
    
    \/\/
     \/
     
    '''
    if get_direction(coord) == "U":
        # ! bottom left
        x,y = coord
        
        up = x+1,y+1
        right = x+2,y
        if up in grid and right in grid and grid[up] == player and grid[right] == player:
            return True
        
        # ! bottom right
        left = x-2,y
        up = x-1,y+1
        if up in grid and left in grid and grid[up] == player and grid[left] == player:
            return True
        
        # ! top
        left = x-1,y-1
        right = x+1,y-1
        if left in grid and right in grid and grid[left] == player and grid[right] == player:
            return True
        return False
    
    else:
        # ! top left
        x,y = coord
        
        down = x+1,y-1
        right = x+2,y
        if down in grid and right in grid and grid[down] == player and grid[right] == player:
            return True
        
        # ! top right
        left = x-2,y
        down = x-1,y-1
        if down in grid and left in grid and grid[down] == player and grid[left] == player:
            return True
        
        # ! bottom
        left = x-1,y+1
        right = x+1,y+1
        if left in grid and right in grid and grid[left] == player and grid[right] == player:
            return True
        return False
    
visited = set()
def count_score(coord,player):
    '''
     /\
    /\/\
    
    \/\/
     \/
     
    '''
    if get_direction(coord) == "U":
        # ! bottom left
        x,y = coord
        
        up = x+1,y+1
        right = x+2,y
        if up in grid and right in grid and grid[up] == player and grid[right] == player:
            return sorted([coord,up,right])
        
        # ! bottom right
        left = x-2,y
        up = x-1,y+1
        if up in grid and left in grid and grid[up] == player and grid[left] == player:
            return sorted([coord,up,left])
        
        # ! top
        left = x-1,y-1
        right = x+1,y-1
        if left in grid and right in grid and grid[left] == player and grid[right] == player:
            return sorted([coord,left,right])
        return False
    
    else:
        # ! top left
        x,y = coord
        
        down = x+1,y-1
        right = x+2,y
        if down in grid and right in grid and grid[down] == player and grid[right] == player:
            return sorted([coord,down,right])
        
        # ! top right
        left = x-2,y
        down = x-1,y-1
        if down in grid and left in grid and grid[down] == player and grid[left] == player:
            return sorted([left,down,coord])
        
        # ! bottom
        left = x-1,y+1
        right = x+1,y+1
        if left in grid and right in grid and grid[left] == player and grid[right] == player:
            return sorted([left,right,coord])
        return False
        

grid[(0,0)] = 0
# grid[(1,0)] = 1
# grid[(-1,0)] = 1
# grid[(0,-1)] = 1
# grid[(-1,0)] = 0u
# grid[(1,0)] = 0
# grid[(1,1)] = 0
# edge = [(-1,0),(-2,0)]

# ! triangle on, triangle connected to 
p,m = map(int,input().split())
traversals = list(map(int,input().split()))
# p1_traversals = 16
# p2_traversals = 2

# edge = [(-1,0),(-2,0)]
positions = [[(0,0),(-1,0)] for i in range(p)]
# for triangle in grid:
#     for player in range(p):
#         if grid[triangle] == player+1:
#             coords = count_score(triangle,player+1)
#             if coords and not tuple(coords) in visited:
#                 print(coords)
#                 # scores[player] += 1
#                 visited.add(tuple(coords)
# exit()
# edge = next_edge(edge)
# print("   ",edge)
# edge = next_edge(edge)
# print("   ",edge)
# edge = next_edge(edge)
# print("   ",edge)
# edge = next_edge(edge)
# print("   ",edge)
# edge = next_edge(edge)
# print("   ",edge)
# edge = next_edge(edge)
# print("   ",edge)

for i in range(m):
    # print("TURN",i)
    player_idx = i % p
    player = player_idx + 1
    # fill_triangle = 
    fill_triangle = tuple(positions[player_idx][1])
    # print(fill_triangle)
    for x in range(traversals[player_idx]):
        positions[player_idx] = next_edge(positions[player_idx])
        if forms_triangle(positions[player_idx][1],player):
            print("STOP")
            break
    grid[fill_triangle] = player
        
    # if i % 2 == 0:
    #     fill_triangle = tuple(p1[1])
    #     for x in range(p1_traversals):
    #         p1 = next_edge(p1)
    #         print("P!",p1)
    #         if forms_triangle(p1[1],1):
    #             print("EARLY STOP")
    #             break
    #     grid[fill_triangle] = 1
    # else:
    #     fill_triangle = tuple(p2[1])
    #     for x in range(p2_traversals):
    #         p2 = next_edge(p2)
    #         print("P2",p2)
    #         if forms_triangle(p2[1],2):
    #             print("EARLY STOP")
    #     grid[fill_triangle] = 2
    
    for i in range(len(positions)):
        if tuple(positions[i][0]) in grid and tuple(positions[i][1]) in grid:
            # print("P1 RESET")
            leftmost = sorted(grid.keys())[0]
            x,y = leftmost
            positions[i] = [leftmost,(x-1,y)]
    print(positions)
    print(grid)
    # print()
    # print(p1,p2,grid)
    # print()

scores = [0] * p
visited = set()
for triangle in grid:
    for player in range(p):
        if grid[triangle] == player+1:
            coords = count_score(triangle,player+1)
            if coords and not tuple(coords) in visited:
                scores[player] += 1
                visited.add(tuple(coords))
    # if grid[triangle] == 2:
    #     # print(triangle)
    #     coords = forms_triangle(triangle,2)
    #     if coords and not coords in visited:
    #         p2_score += 1
for score in scores:
    print(score)

perimeter = 0
leftmost = sorted(grid.keys())[0]
x,y = leftmost
leftmost = [list(leftmost),[x-1,y]]
edge = next_edge(leftmost)
# print(leftmost)
while edge != leftmost:
    edge = next_edge(edge)
    perimeter += 1
print(perimeter+1)
        
'''
11
11?
 111
'''


# edge = next_edge(edge)
# print(edge)
# edge = next_edge(edge)
# print(edge)
# print(grid[0,0].get_edges())

# for x in range(3):
#     for y in range(3):
#         print(x,y,get_direction((x,y)))
        
        

    

