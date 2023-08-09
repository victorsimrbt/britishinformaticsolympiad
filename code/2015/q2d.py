from itertools import combinations
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
        if 0 <= square[0] <= 4 and 0 <= square[1] <= 4 and not(square in occupied):
            pass
        else:
            return False
        adjacent_points = adjacent(square)
        for point in adjacent_points:
            if point in occupied:
                return False
    return True

ships = [4,3,2,1]
orientations = ['H','V']
coords = []
possibilities = []
for x in range(5):
    for y in range(5):
        possibilities.append([x,y,'H'])
        possibilities.append([x,y,'V'])

four_pos = []
for pos in possibilities:
    occupied = []
    x,y,orientation = pos
    occupied_squares = occupying_squares(4,[x,y],orientation)
    if valid(occupied_squares):
        four_pos.append(pos)

three_pos = []
for pos in possibilities:
    occupied = []
    x,y,orientation = pos
    occupied_squares = occupying_squares(3,[x,y],orientation)
    if valid(occupied_squares):
        three_pos.append(pos)
        
two_pos = []
for pos in possibilities:
    occupied = []
    x,y,orientation = pos
    occupied_squares = occupying_squares(2,[x,y],orientation)
    if valid(occupied_squares):
        two_pos.append(pos)
        
one_pos = []
for pos in possibilities:
    occupied = []
    x,y,orientation = pos
    occupied_squares = occupying_squares(1,[x,y],orientation)
    if valid(occupied_squares):
        one_pos.append(pos)

possible_pos = 0
for pos in four_pos:
    occupied = []
    x,y,orientation = pos
    occupied_squares = occupying_squares(4,[x,y],orientation)
    for square in occupied_squares:
        occupied.append(square)
    for pos in three_pos:
        x,y,orientation = pos
        occupied_squares = occupying_squares(3,[x,y],orientation)
        if valid(occupied_squares):
            for square in occupied_squares:
                occupied.append(square)
            for pos in two_pos:
                x,y,orientation = pos
                occupied_squares = occupying_squares(2,[x,y],orientation)
                if valid(occupied_squares):
                    for square in occupied_squares:
                        occupied.append(square)
                    for pos in one_pos:
                        x,y,orientation = pos
                        occupied_squares = occupying_squares(1,[x,y],orientation)
                        if valid(occupied_squares):
                            for square in occupied_squares:
                                occupied.append(square)
                            print(occupied)
                            possible_pos += 1
           

print(possible_pos)






