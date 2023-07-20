import numpy as np

edges = {}
grid = [[[] for i in range(5)] for i in range(5)]
# row, column, edge
grid[0][0] = [[0,0,1],[0,0,2],[0,0,3],[0,0,4],[0,0,5],[0,0,6]]
grid[0][1] = [[0,1,1],[0,1,2],[0,1,3],[0,1,4],[0,0,2],[0,1,6]]
grid[0][2] = [[0,2,1],[0,2,2],[0,2,3],[0,2,4],[0,1,2],[0,2,6]]
grid[0][3] = [[0,3,1],[0,3,2],[0,3,3],[0,3,4],[0,2,2],[0,3,6]]
grid[0][4] = [[0,4,1],[0,4,2],[0,4,3],[0,4,4],[0,3,2],[0,4,6]]

grid[1][0] = [[0,1,4],[1,0,2],[1,0,3],[1,0,4],[1,0,5],[0,0,3]]
grid[1][1] = [[0,2,4],[1,1,2],[1,1,3],[1,1,4],[1,0,2],[0,1,3]]
grid[1][2] = [[0,3,4],[1,2,2],[1,2,3],[1,2,4],[1,1,2],[0,2,3]]
grid[1][3] = [[0,4,4],[1,3,2],[1,3,3],[1,3,4],[1,2,2],[0,3,3]]
grid[1][4] = [[1,4,1],[1,4,2],[1,4,3],[1,4,4],[1,3,2],[0,4,3]]

grid[2][0] = [[1,0,4],[2,0,2],[2,0,3],[2,0,4],[2,0,5],[2,1,6]]
grid[2][1] = [[1,1,4],[2,1,2],[2,1,3],[2,1,4],[2,0,2],[1,0,3]]
grid[2][2] = [[1,2,4],[2,2,2],[2,2,3],[2,2,4],[2,1,2],[1,1,3]]
grid[2][3] = [[1,3,4],[2,3,2],[2,3,3],[2,3,4],[2,2,2],[1,2,3]]
grid[2][4] = [[1,4,4],[2,4,2],[2,4,3],[2,4,4],[2,3,2],[1,3,3]]

grid[3][0] = [[2,1,4],[3,0,2],[3,0,3],[3,0,4],[3,0,5],[2,0,3]]
grid[3][1] = [[2,2,4],[3,1,2],[3,1,3],[3,1,4],[3,0,2],[2,1,3]]
grid[3][2] = [[2,3,4],[3,2,2],[3,2,3],[3,2,4],[3,1,2],[2,2,3]]
grid[3][3] = [[2,4,4],[3,3,2],[3,3,3],[3,3,4],[3,2,2],[2,3,3]]
grid[3][4] = [[2,4,1],[3,4,2],[3,4,3],[3,4,4],[3,3,2],[2,4,3]]

grid[4][0] = [[3,0,4],[4,0,2],[4,0,3],[4,0,4],[4,0,5],[4,1,6]]
grid[4][1] = [[3,1,4],[4,1,2],[4,1,3],[4,1,4],[4,0,2],[3,0,3]]
grid[4][2] = [[3,2,4],[4,2,2],[4,2,3],[4,2,4],[4,1,2],[3,1,3]]
grid[4][3] = [[3,3,4],[4,3,2],[4,3,3],[4,3,4],[4,2,2],[3,2,3]]
grid[4][4] = [[3,4,4],[4,4,2],[4,4,3],[4,4,4],[4,3,2],[3,3,3]]

def coord_to_num(x,y):
    return 5*x+y+1

hexagons = [None,]
for a in range(5):
    for b in range(5):
        hexagons.append(grid[a][b])
        
        

# print("HEY",hexagons[1][3])
    
r,b = map(int,input().split())
s,f = map(int,input().split())
# r = 9
# b = 3

# s = 3
# f = 1

red_pos = 1
red_face = 1

blue_pos = 25
blue_face = 6

def skirmish():
    global red_pos,red_face
    global blue_pos,blue_face
    # print(red_pos,red_face)
    # print(blue_pos,blue_face)
    
    
    edges[tuple(hexagons[red_pos][red_face-1])] = "R"
    edges[tuple(hexagons[blue_pos][blue_face-1])] = "B"
    
    red_face = red_face % 6 + 1
    blue_face = blue_face - 1
    if blue_face == 0:
        blue_face = 6
    
    red_pos = (red_pos+r) - 25 if red_pos+r > 25 else red_pos+r
    blue_pos = (blue_pos+b) - 25 if blue_pos+b > 25 else blue_pos+b
    
def red_feud():
    global edges
    # ! edge is unowned
    options = []
    hex_num = 0
    for hexagon in hexagons[1:]:
        hex_num += 1
        edge_num = 0
        for edge in hexagon:
            edge_num += 1
            # check if edge will yield control
            if not tuple(edge) in edges:
                win_hexagon = 0
                take_hexagon = 0
                
                for hexagon2 in hexagons[1:]:
                    # print(hexagon2)
                    if edge in hexagon2:
                        red_edges = len([val for val in hexagon2 if tuple(val) in edges and edges[tuple(val)] == "R"])
                        blue_edges = len([val for val in hexagon2 if tuple(val) in edges and edges[tuple(val)] == "B"])
                        if red_edges + 1 > blue_edges and not(red_edges > blue_edges):
                            win_hexagon += 1
                        if blue_edges > red_edges and red_edges+1 == blue_edges:
                            take_hexagon += 1
                options.append([win_hexagon,take_hexagon,-hex_num,-edge_num])
    options.sort()
    if options:
        move = options[-1]
        _,_,hex_num,edge_num = move
        # print(move)
        # edges[(0,3,2)] = 1
        edges[tuple(hexagons[abs(hex_num)][abs(edge_num)-1])] = "R"

def blue_feud():
    global edges
    # ! edge is unowned
    options = []
    hex_num = 0
    for hexagon in hexagons[1:]:
        hex_num += 1
        edge_num = 0
        for edge in hexagon:
            edge_num += 1
            # check if edge will yield control
            if not tuple(edge) in edges:
                win_hexagon = 0
                take_hexagon = 0
                
                for hexagon2 in hexagons[1:]:
                    # print(hexagon2)
                    if edge in hexagon2:
                        red_edges = len([val for val in hexagon2 if tuple(val) in edges and edges[tuple(val)] == "R"])
                        blue_edges = len([val for val in hexagon2 if tuple(val) in edges and edges[tuple(val)] == "B"])
                        if blue_edges + 1 > red_edges and not(blue_edges > red_edges):
                            win_hexagon += 1
                        if red_edges > blue_edges and blue_edges+1 == red_edges:
                            take_hexagon += 1
                options.append([win_hexagon,take_hexagon,hex_num,edge_num])
    options.sort()
    if options:
        move = options[-1]
        _,_,hex_num,edge_num = move
        # print(move)
        # edges[(0,3,2)] = 1
        edges[tuple(hexagons[abs(hex_num)][abs(edge_num)-1])] = "B"
            
        
    
# def feud():
    

for i in range(s):
    skirmish()
    # print()

for i in range(f):
    red_feud()
    blue_feud()
    
    
red_score = 0
blue_score =0
for hexagon in hexagons[1:]:
    red_edges = len([val for val in hexagon if tuple(val) in edges and edges[tuple(val)] == "R"])
    blue_edges = len([val for val in hexagon if tuple(val) in edges and edges[tuple(val)] == "B"])
    if red_edges > blue_edges:
        red_score += 1
    if blue_edges > red_edges:
        blue_score += 1

print(red_score)
print(blue_score)

# print(hexagons[25][5])
# print(hexagons[19][2])
# print(edges[tuple(hexagons[25][5])])
    
    
    
    
    
    




# ? 10 on each horizontal (5 horizontals)
# ? 6 on each vertical (5 verticals)