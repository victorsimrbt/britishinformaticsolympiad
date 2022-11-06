# Locate quads
# Track position with quad movement. If touching input coord stop. 
import numpy as np
move_dict = {
    "R" : np.array([-1,0]),
    "L" : np.array([1,0]),
    "D" : np.array([0,1]),
    "U" : np.array([0,-1])
}

def diamond_width(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return diamond_width(n-1)*2+1

def locate_quad(coord,centre):
    new_coord = coord[:]
    new_coord[0] -= centre[0]
    new_coord[1] -= centre[1]
    x,y = new_coord
    if y < x and y > -x:
        return "R"
    if y > x and y < -x:
        return "L"
    if y > x and y > -x:
        return "U"
    if y < x and y < -x:
        return "D"
    
def find_quads(coord,centre,n):
    width = round((diamond_width(n)-1)/2/2)
    quad = locate_quad(coord,centre)
    new_centre = centre
    if quad == "R":
        new_centre = [centre[0]+width,centre[1]]
    if quad == "L":
        new_centre = [centre[0]-width,centre[1]]
    if quad == "U":
        new_centre = [centre[0],centre[1]+width]
    if quad == "D":
        new_centre = [centre[0],centre[1]-width]
    return coord,new_centre,quad

