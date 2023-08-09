import numpy as np
from matplotlib import pyplot as plt

F = [[1,0],[2,0],[0,-1],[1,-1],[1,-2]]
G = [[0,0],[1,0],[1,-1],[1,-2],[2,-1]]
I = [[0,0],[0,-1],[0,-2],[0,-3],[0,-4]]
L = [[0,0],[0,-1],[0,-2],[0,-3],[1,-3]]
J = [[1,0],[1,-1],[1,-2],[1,-3],[0,-4]]
N = [[1,0],[0,-1],[1,-1],[0,-2],[0,-3]]
M = [[0,0],[0,-1],[1,-1],[1,-2],[1,-3]]
P = [[0,0],[1,0],[0,-1],[1,-1],[0,-2]]
Q = [[0,0],[1,0],[0,-1],[1,-1],[1,-2]]
T = [[0,0],[1,0],[2,0],[1,-1],[1,-2]]
U = [[0,0],[0,-1],[3,0],[1,-1],[2,-1]]
V = [[0,0],[0,-1],[0,-2],[1,-2],[2,-2]]
W = [[0,0],[0,-1],[1,-1],[1,-2],[2,-2]]
X = [[1,0],[0,-1],[1,-1],[1,-2],[2,-1]]
Z = [[0,0],[1,0],[1,-1],[1,-2],[2,-2]]
S = [[1,0],[2,0],[1,-1],[1,-2],[0,-2]]
Y = [[1,0],[0,-1],[1,-1],[1,-2],[1,-3]]
A = [[0,0],[0,-1],[0,-2],[0,-3],[1,-1]]

points = {}
input_translation = {
    "F" : F,
    "G" : G,
    "I" : I,
    "L" : L,
    "J" : J,
    "N" : N,
    "M" : M,
    "P" : P,
    "Q" : Q,
    "T" : T,
    "U" : U,
    "V" : V,
    "W" : W,
    "Z" : Z,
    "S" : S,
    "Y" : A,
    
}
    
colours = ["R","B"]
def neighbors(coord):
    adjacent = []
    x,y= coord
    adjacent.append([x,y+1])
    adjacent.append([x+1,y])
    adjacent.append([x,y-1])
    adjacent.append([x-1,y])
    return adjacent

def place_shape(shape,base_coord,points,marker):
    shape_points = np.array(shape) + np.array(base_coord)
    for point in shape_points:
        points[tuple(point)] = marker
        # grid[point[0]][point[1]] = marker
    return points
        
def check_valid(shape_1,shape_2):
    for point in shape_1:
        if point in shape_2:
            return False
    for point in shape_1:
        adj = neighbors(point)
        for neighbor in adj:
            if tuple(neighbor) in shape_2:
                return True
    return False

def plot_shape(points):
    for point in points:
        x,y = point
        plt.scatter(x,y)

def fuse_points(shape_1,shape_2):
    master_points = {}
    for point in shape_1:
        master_points[point] = 1
    for point in shape_2:
        master_points[point] = 1
    return master_points

def secondelem(a):
    return [a[1],a[0]]

def normalize(grid):
    def secondelem(a):
        return a[1]
    points = [point for point in grid.keys()]
    points = sorted(sorted(points,key=secondelem))
    base_coord = points[0]
    normalize_op =  np.array([0,0]) - np.array(base_coord)
    points = np.array(points) + normalize_op
    points = [list(point) for point in points]
    return points

print("NAME: VICTOR SIM")
print("YEAR: 11")
print("SCHOOL: WICHESTER COLLEGE")
shape_1,shape_2 = input()
shap1 = input_translation[shape_1]
shap2 = input_translation[shape_2]
valid = 0
configs = []
original =[]
for x in range(-5,6):
    shape_1 = place_shape(shap1,[0,0],{},1)
    for y in range(-5,6):
        shape_2 = place_shape(shap2,[x,y],{},2)
        if check_valid(shape_1,shape_2):
            grid = fuse_points(shape_1,shape_2)
            orig = [key for key in grid.keys()]
            grid = list(normalize(grid))
            # print(grid,configs)
            if not(sorted(grid) in configs):
                configs.append(sorted(grid))
                original.append(orig)
                valid += 1
print(valid)