'''
each triangle is a coordinate
each edge is described by 4 numbers, triangle 1 and triangle 2
seems like traversing edges clockwise works for all cases
will test
'''
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
    print("GETTING",edge)
    # ! assumes that edge is on perimeter (wrong assumption )
    
    tri1,tri2 = edge
    tri1,tri2 = list(tri1),list(tri2)
    tri1_edges = get_edges(tri1)
    while tri1_edges[0] != tri2:
        tri1_edges.append(tri1_edges.pop(0))
        # print("Etri1_edges)
    # print(tri1_edges)
    for tri_edge in tri1_edges[1:]:
        # ! check if edge occupied
        if tuple(tri_edge) in grid:
            print("OCCUPIED")
            # ! is occupied
            # ! if it is occupied, keep getting new edge until u get a valid one
            new_triangle = tri_edge
            new_triangle_edges = get_edges(new_triangle)
            start_edge = new_triangle_edges.index(tri1)
            next_val = new_triangle_edges[(start_edge + 1) % 3]
            break
            # if next_val in
            # return [tri_edge,new_triangle_edges[next_val]]
        else:
            return [tri1,tri_edge]
    
    if tuple(next_val) in grid:
        return next_edge((tri_edge,next_val))
    else:
        return [tri_edge,next_val]

grid[(0,0)] = 0
grid[(-1,0)] = 0
grid[(0,-1)] = 0
grid[(1,0)] = 0
# grid[(1,1)] = 0
# edge = [(-1,0),(-2,0)]

# ! triangle on, triangle connected to 
p1 = [(0,0),(-1,0)]
p2 = [(0,0),(-1,0)]

p1_traversals = 16
p2_traversals = 2

edge = [(-1,0),(-2,0)]
edge = next_edge(edge)
print("   ",edge)
edge = next_edge(edge)
print("   ",edge)

# for i in range(2):
#     print("TURN",i)
#     if i % 2 == 0:
#         fill_triangle = tuple(p1[1])
#         for x in range(p1_traversals):
#             p1 = next_edge(p1)
#         grid[fill_triangle] = 1
#     else:
#         fill_triangle = tuple(p2[1])
#         for x in range(p2_traversals):
#             p2 = next_edge(p2)
#         grid[fill_triangle] = 2
    
            
#     if tuple(p1[0]) in grid and tuple(p1[1]) in grid:
#         print("P1 RESET")
#         leftmost = sorted(grid.keys())[0]
#         x,y = leftmost
#         p1 = [leftmost,(x-1,y)]
        
#     if tuple(p2[0]) in grid and tuple(p2[1]) in grid:
#         print("P2 RESET")
#         leftmost = sorted(grid.keys())[0]
#         x,y = leftmost
#         p2 = [leftmost,(x-1,y)]
        
#     print(p1,p2,grid)
#     print()
    


# edge = next_edge(edge)
# print(edge)
# edge = next_edge(edge)
# print(edge)
# print(grid[0,0].get_edges())

# for x in range(3):
#     for y in range(3):
#         print(x,y,get_direction((x,y)))
        
        

    

