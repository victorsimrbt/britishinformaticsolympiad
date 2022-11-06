import numpy as np
# Bottom left is (0,0)

occupied = []
a,c,m = [int(val) for val in input().split()]
r = 0
ships = [4,3,3,2,2,2,1,1,1,1]


def coord_to_idx(coord):
    x,y = coord
    row,column = 9-y,x
    return row,column
    2

def adjacent(point):
    x,y = point
    coords = [[x-1,y-1],
              [x-1,y],
              [x-1,y+1],
              [x,y-1],
              [x,y+1],
              [x+1,y-1],
              [x+1,y],
              [x+1,y+1]]
    return coords
    

def occupying_squares(ship_size,coord,orientation):
    x,y = coord
    orientation_dict = {
    "H" : [[x,y],[x+1,y],[x+2,y],[x+3,y]],
    "V" : [[x,y],[x,y+1],[x,y+2],[x,y+3]],
    }
    occupied_squares = orientation_dict[orientation][:ship_size]
    return occupied_squares

def valid(occupied_squares):
    for square in occupied_squares:
        if 0 <= square[0] <= 9 and 0 <= square[1] <= 9 and not(square in occupied):
            pass
        else:
            return False
        adjacent_points = adjacent(square)
        for point in adjacent_points:
            if point in occupied:
                return False
    return True

while ships:
    ship_size = ships.pop(0)
    while True:
        r = (a*r+c)%m
        r_string = list(str(r))
        while len(r_string) < 2:
            r_string.insert(0,0)
        coord = int(r_string[-1]),int(r_string[-2])
        r = (a*r+c)%m
        orientation = ['H' if r % 2 == 0 else 'V'][0]
        occupied_squares = occupying_squares(ship_size,coord,orientation)
        if valid(occupied_squares):
            for square in occupied_squares:
                occupied.append(square)
            print(int(r_string[-1]),int(r_string[-2]),orientation)
            break
    #print(occupied)
    #print(x,y,direction)
