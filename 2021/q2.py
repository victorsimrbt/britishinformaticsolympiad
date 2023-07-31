edge = []
# markers = {(-1,0):1, (0,0):0, (-2,0):2}
# triangles = [[0,0],[-1,0],[-2,0]] # clockwise
# direction = {(0,0) : 1, (-1,0) : 0, (-2,0): 1} # 1 for up 0 for down
markers = {(0,0):0}
# direction = {(0,0) : 1} # 1 for up 0 for down
# markers = {(-1,0):1, (0,0):0}
# triangles = [[0,0],[-1,0]] # clockwise
# direction = {(0,0) : 1, (-1,0) : 0} # 1 for up 0 for down
outer_edges = []

score = [0,0,0]

def tri_dir(coord):
    if sum(coord) % 2 == 0:
        return 1
    else:
        return 0

def neighbor(triangle_coord):
    x,y = triangle_coord
    adjacent = []
    if tri_dir(triangle_coord) == 1:
        adjacent.append([x-1,y])
        adjacent.append([x+1,y])
        adjacent.append([x,y-1])
    else:
        adjacent.append([x,y+1])
        adjacent.append([x+1,y])
        adjacent.append([x-1,y])
    return adjacent

traversal_order = []

def is_inside(edge):
    tri_1,tri_2 = edge
    if tuple(tri_1) in markers and tuple(tri_2) in markers:
        return True
    else:
        return False

units_traversed = 0
def traverse(start_edge,traversals,player):
    units_traversed = 0
    
    original_edge = start_edge
    triangle_1,triangle_2 = start_edge
    filled_triangle = [triangle for triangle in start_edge if tuple(triangle) in markers][0]
    first_filled = filled_triangle
    # print("FILLED TRIANGLE",filled_triangle)
    while units_traversed < traversals:
        # print("START",start_edge)
        adj = neighbor(filled_triangle)
        edges = [sorted([filled_triangle,neighbor]) for neighbor in adj]
        # print(edges)
        
        start_idx = edges.index(sorted(start_edge))
        for i in range(1,3):
            if units_traversed == traversals:
                break
            start_edge = edges[(start_idx+i)%3]
            # print("  ",i,start_edge)
            if is_inside(start_edge):
                filled_triangle = [triangle for triangle in start_edge if triangle != filled_triangle][0]
                # print("INSIDE",filled_triangle)
                break
            else:
                empty_triangle = [triangle for triangle in start_edge if not(tuple(triangle) in markers)]
                # print(empty_triangle)
                if can_score(empty_triangle,player):
                    # print("CAN SCORE!")
                    score[player] += 1
                    units_traversed = 100000
                    break
                units_traversed += 1
                # print(units_traversed,start_edge,"traversed")
    
    empty_triangle = [triangle for triangle in original_edge if not(tuple(triangle) in markers)][0]
    markers[tuple(empty_triangle)] = player
    return start_edge

def reset_position(position):
    triangles = markers.keys()
    leftest = list(sorted(triangles)[0])
    if is_inside(position):
        edges = neighbor(leftest)
        # print("RESET")
        empty_edge = sorted([edge for edge in edges if not(tuple(edge) in markers)])
        return [leftest,empty_edge[0]]
    return position

def can_score(triangle,player):
    triangle = triangle[0]
    x,y = triangle
    if tri_dir(triangle) == 1:
        left_triangle = [
            [x-2,y],
            [x-1,y+1]
        ]
        right_triangle = [
            [x+2,y],
            [x+1,y+1]
        ]
        down_triangle = [
            [x-1,y-1],
            [x+1,y-1]
        ]
        triangles = [left_triangle,right_triangle,down_triangle]
    else:
        left_triangle = [
            [x-2,y],
            [x-1,y-1]
        ]
        right_triangle = [
            [x+2,y],
            [x+1,y-1]
        ]
        down_triangle = [
            [x-1,y+1],
            [x+1,y+1]
        ]
        triangles = [left_triangle,right_triangle,down_triangle]
    # print(triangles)
    for big_triangle in triangles:
        filled = [True if tuple(small_triangle) in markers and markers[tuple(small_triangle)] == player else 0 for small_triangle in big_triangle]
        if filled.count(True) == 2:
            return True
    return False
        
        
    
    
    
# def is_connected(edge_1,edge_2):
#     tri_1,t
# print("THIS",traverse([[0,0],[1,0]]))
# outer_edges = sorted(outer_edges)
p,m = [int(char) for char in input().split()]
traversals = [0]+[int(char) for char in input().split()]
positions = [[[-1,0],[0,0]],
             [[-1,0],[0,0]],
             [[-1,0],[0,0]],
             [[-1,0],[0,0]],
             [[-1,0],[0,0]]]

def print_triangles():
    for triangle in markers:
        print(triangle,":",markers[tuple(triangle)])


turn = 0
for i in range(5):
    turn %= p
    turn += 1
    # print("TURN",turn)
    positions[turn] = traverse(positions[turn],traversals[turn],turn)
    for i in range(1,p+1):
        positions[i] = reset_position(positions[i])
    # if turn == 1:
    #     p1_position = traverse(p1_position,p1_traversals,turn)
    # if turn == 2:
    #     p2_position = traverse(p2_position,p2_traversals,turn)
    # p1_position = reset_position(p1_position)
    # p2_position = reset_position(p2_position)
    # print(p1_position,p2_position)
    # print_triangles()

for i in range(1,p+1):
    print(score[i])

outer_edges = []
# print(markers)
for triangle in markers.keys():
    neighbors = neighbor(triangle)
    # print(triangle,neighbors)
    for adj in neighbors:
        if not(tuple(adj) in markers) and not(sorted([list(triangle),list(adj)]) in outer_edges):
            # print(triangle,adj)
            outer_edges.append(sorted([list(triangle),list(adj)]))
print(len(outer_edges))



'''
define edge as intersection between two triangles
outer edges are edges who are connected to empty triangles  

traversal:
    move through each edge 
'''