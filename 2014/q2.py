def tile_1(points,edges):
    edges[points[0]][points[2]] = 1
    edges[points[2]][points[0]] = 1
    
    edges[points[1]][points[3]] = 2
    edges[points[3]][points[1]] = 2
    return edges

def tile_2(points,edges):
    edges[points[0]][points[2]] = 2
    edges[points[2]][points[0]] = 2
    
    edges[points[1]][points[3]] = 1
    edges[points[3]][points[1]] = 1
    return edges

def tile_3(points,edges):
    edges[points[0]][points[3]] = 1
    edges[points[3]][points[0]] = 1
    
    edges[points[1]][points[2]] = 2
    edges[points[2]][points[1]] = 2
    return edges

def tile_4(points,edges):
    edges[points[0]][points[1]] = 1
    edges[points[1]][points[0]] = 1
    
    edges[points[3]][points[2]] = 2
    edges[points[2]][points[3]] = 2
    return edges

def tile_5(points,edges):
    edges[points[2]][points[1]] = 1
    edges[points[1]][points[2]] = 1
    
    edges[points[3]][points[0]] = 2
    edges[points[0]][points[3]] = 2
    return edges

def tile_6(points,edges):
    edges[points[2]][points[3]] = 1
    edges[points[3]][points[2]] = 1
    
    edges[points[1]][points[0]] = 2
    edges[points[0]][points[1]] = 2
    return edges

def print_edges(edges):
    for a in range(len(edges)):
        for b in range(len(edges[0])):
            if edges[a][b]:
                print(a,",",b,":",edges[a][b])

tile_functions = [tile_1,tile_2,tile_3,tile_4,tile_5,tile_6]
grid_size = int(input())
num_points = grid_size**2 * 4 - grid_size**2
grid_inc=  grid_size*2 + 1
edges = []
for i in range(num_points):
    edges.append([0 for i in range(num_points)])
for a in range(grid_size):
    tile_row = [int(char) for char in input().split()]
    for b in range(len(tile_row)):
        base = grid_inc*a+b
        points = [base,base+(grid_size+1),base+(grid_size*2+1),base+(grid_size)]
        tile_function = tile_functions[tile_row[b]-1]
        edges = tile_function(points,edges)

# print_edges(edges)
def find_loops(start,color):
    # color is 1 or 0
    loops = []
    queue = []
    queue.append([start,[]])
    head = 0
    while head < len(queue):
        last = queue[head][0]
        path = queue[head][1]
        head += 1
        for neighbor in range(num_points):
            if edges[last][neighbor] == color:
                updated_path = path+[neighbor]
                if neighbor == start:
                    if len(updated_path) > 2:
                        loops.append(sorted(updated_path))
                    break
                if not(neighbor in path):
                    queue.append([neighbor,updated_path])
    return loops

red = 0
green = 0
loops = []
for i in range(num_points):
    red_loops = find_loops(i,1)
    green_loops = find_loops(i,2)
    for loop in red_loops:
        if not(loop in loops):
            red += len(loop)
            loops.append(loop)
    for loop in green_loops:
        if not(loop in loops):
            green += len(loop)
            loops.append(loop)
print(red,green)

'''
initialize adjacency matrix
tile_functions = [tile_1,tile_2,tile_3,tile_4,tile_5,tile_6]
edges = [40][40]
tiles = []
for a in range(4):
    tile_row = [int(char) for char in input().split()]
    for tile in tile_row:
        tiles.append(tile)

for i in range(len(tiles)):
    points = [i,i+5,i+9,i+4] (CLOCKWISE!!!)
    tile_function = tiles[i]-1
    edges = tile_function(points,edges) (assign edges both ways)

def find_loops(start,color):
    # color is 1 or 0
    loops = []
    queue = []
    queue.append([start,[]])
    head = 0
    while head < len(queue):
        last = queue[head]
        path = queue[head]
        head += 1
        for neighbor in edges[last]:
            if edges[last][neighbor] == color:
                updated_path = path+neighbor
                if neighbor == start:
                    loops.append(updated_path)
                if not(neighbor in path):
                    queue.append([neighbor,updated_path])
    return loops

red = 0
green = 0
for i in range(40):
    red_loops = find_loops(start,"r")
    green_loops = find_loops(start,"r")
    for loop in red_loops:
        red += len(loop)
    for loop in green_loops:
        green += len(loop)

'''