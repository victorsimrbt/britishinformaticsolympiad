'''
trail = {}

directions = [U,R,D,L] (number between 0 and 3)
if turn right, move forwards in list
if turn left, move backwards

up = [U,R,D,L]
left = [L,U,R,D]
right = [R,D,L,U]
down = [D,L,U,R]

def adj(square):
    return (U,R,D,L)
    
every turn:
    check which list it is using
    use the list to determine true direction
    for square in trail, if the turn - trail_score is larger than allowed then move
    otherwise, keep moving right (along the list until the square does not have a trail)
    trail[coord] = allowed
'''

t,i,m = input().split()
t = int(t)
m = int(m)

trail = {}
directions = [0,1,2,3]

up = [0,1,2,3]
right = [1,2,3,0]
down = [2,3,0,1]
left = [3,0,1,2]

directions = [up,right,down,left]

def adj(x,y):
    # ! Up ,right down left
    adjacent = [
        [x,y+1],
        [x+1,y],
        [x,y-1],
        [x-1,y]
    ]
    return adjacent

order_to_idx = {
    "F" : 0,
    "L" : 3,
    "R" : 1,
}


direction = 0
pos = [0,0]
turn = 0

trail[(0,0)] = 0
# ! 0 to 3 (inc), up, right , down, left
for x in range(m):
    order = directions[direction]
    adjacent = adj(pos[0],pos[1])
    
    idx = order[order_to_idx[i[turn % len(i)]]]
    original_idx = idx
    
    while True:
        move = tuple(adjacent[idx])
        if not move in trail or turn - trail[move] > t:
            pos = move
            direction = idx
            trail[move] = turn
            break
        idx = (idx + 1)%4
        if idx == original_idx:
            print("DIE")
            print(pos)
            exit()
    # print(pos,direction)
    turn += 1
print(pos,trail)
    