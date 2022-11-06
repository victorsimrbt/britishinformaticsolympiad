tiles = [
    [[0,1,0],
     [-1,2,-1],
     [0,1,0]],
    [[0,-1,0],
     [1,2,1],
     [0,-1,0]],
    [[0,1,0],
     [1,2,-1],
     [0,-1,0]],
    [[0,1,0],
     [-1,2,1],
     [0,-1,0]],
    [[0,-1,0],
     [-1,2,1],
     [0,1,0]],
    [[0,-1,0],
     [1,2,-1],
     [0,1,0]]]

print_tile = [
    [["_","R","_"],
     ["G","_","G"],
     ["_","R","_"]],
    
    [["_","G","_"],
     ["R","_","R"],
     ["_","G","_"]],
    
    [["_","R","_"],
     ["R","_","G"],
     ["_","G","_"]],
    
    [["_","R","_"],
     ["G","_","R"],
     ["_","G","_"]],
    
    [["_","G","_"],
     ["G","_","R"],
     ["_","R","_"]],
    
    [["_","G","_"],
     ["R","_","G"],
     ["_","R","_"]]]

def print_tiles(config):
    for row in range(len(config)):
        row_tiles = config[row]
        for i in range(3):
            print_line = ''
            for tile in row_tiles:
                tile_values = print_tile[tile-1]
                print_line += ''.join([str(value) for value in tile_values[i]])
            print(print_line)

def binary_tile(config):
    for row in range(len(config)):
        row_tiles = config[row]
        for i in range(3):
            print_line = ''
            for tile in row_tiles:
                tile_values = tiles[tile-1]
                print_line += ' '.join([str(value) for value in tile_values[i]])
            print(print_line)
            
def interesting_neighbours(point,grid):
    x,y = point
    neighbour_points = [[x-1,y-1],
                        [x-1,y],
                        [x-1,y+1],
                        [x,y-1],
                        [x,y+1],
                        [x+1,y-1],
                        [x+1,y],
                        [x+1,y+1]]
    valid_points = [point for point in neighbour_points if 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid)]
    interesting_points = []
    for point in valid_points:
        if (grid[point[0]][point[1]] == grid[x][y] or grid[point[0]][point[1]] == 2) and grid[point[0]][point[1]] != 0:
            interesting_points.append(point)
    return interesting_points
            
def find_loops(grid):
    visited = []
    queue = [[[0,1],[[0,1]]]]
    
    for value in queue:
        path = value[1]
        neighbours = interesting_neighbours(value[0],grid)
        
        for neighbour in neighbours:
            if not(neighbour in visited):
                visited.append(neighbour)
                new_path = path[:]
                new_path.append(neighbour)
                new_node = [neighbour] + [new_path]
                queue.append(new_node)
    return queue
      
config = []
size = int(input())
for i in range(size):
    config.append([int(value) for value in input().split()])
    
grid = []
for row in range(len(config)):
    row_tiles = config[row]
    for i in range(3):
        row_values = []
        for tile in row_tiles:
            tile_values = tiles[tile-1]
            row_values += [int(value) for value in tile_values[i]]
        grid.append(row_values)

print(find_loops(grid))
