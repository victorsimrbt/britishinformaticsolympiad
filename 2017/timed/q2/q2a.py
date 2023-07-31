'''
edges are 2d array with [a,b] meaning dot a and b are connected
squares is an array with each square consisting of 4 edges

def move():
    update player position
    get adjacent points in clockwise order
    if player 2, reverse order (but upwards first)
    for edge in edge:
        check if edge is occupied
        if not:
            add edge 
    if square completed then play another turn

def check_square():
    check if 4 edges of square are covered by same
    if so, return player
    else:
    return none
    
rtq + focus issues
'''
squares = []
square_vals = ["*" for i in range(25)]
for x in range(30):
    
    top_left = x+1
    if not top_left in [6,12,18,24,30,36]:
        square = [top_left,top_left + 1,top_left + 6, top_left + 7]
        print(square)
        squares.append(square)
# print(len(squares))
# exit()
p1,m1,p2,m2,t = map(int,"4 10 14 23 47".split())
edges = [[0 for a in range(37)] for b in range(37)]


def coord_to_num(x,y):
    return 6*y + x + 1

# print("YEAH",coord_to_num(5,5))

def num_to_coord(num):
    num -= 1
    return num % 6,num // 6

def check_squares():
    
    for i in range(len(squares)):
        tl,tr,bl,br = squares[i]
        print(i,tl,tr,bl,br)
        square_edges = [edges[tl][tr],edges[tl][bl],edges[bl][br],edges[tr][br]]
        print(square_edges)
        if square_edges.count(1) == len(square_edges):
            square_vals[i] = "X"
        elif square_edges.count(2) == len(square_edges):
            square_vals[i] = "O"
        else:
            square_vals[i] = "*"

print(squares)
print(square_vals)
check_squares()
# # tl tr
# edges[1][2] = 1
# edges[2][1] = 1

# # tl bl
# edges[1][7] = 1
# edges[7][1] = 1

# #bl br
# edges[8][7] = 1
# edges[7][8] = 1

# #tr br
# edges[8][2] = 1
# edges[2][8] = 1
# check_squares()
# print(square_vals)
# exit()
def p1_adj(x,y):
    '''
      (x,y-1)
        |
    --(x,y)--
        |
    '''
    adj = [
        [x,y-1],
        [x+1,y],
        [x,y+1],
        [x-1,y],
    ]
    adj = [pt for pt in adj if pt[0] >= 0 and pt[0] <= 5 and pt[1] >= 0 and pt[1] <= 5]
    return adj

def p2_adj(x,y):
    '''
      (x,y-1)
        |
    --(x,y)--
        |
    '''
    adj = [
        [x,y-1],
        [x-1,y],
        [x,y+1],
        [x+1,y],
    ]
    adj = [pt for pt in adj if pt[0] >= 0 and pt[0] <= 5 and pt[1] >= 0 and pt[1] <= 5]
    return adj

def p1_move():
    global p1,m1
    p1 += m1
    while True:
        if p1 > 36:
            p1 -= 36
        p1_coord = num_to_coord(p1)
        options = p1_adj(p1_coord[0],p1_coord[1])
        print(options)
        original_squares = square_vals[:]
        for edge in options:
            x,y = edge
            dot2 = coord_to_num(x,y)
            # print(p1,dot2)
            if edges[p1][dot2] == False and edges[dot2][p1] == False:
                print("P1 connects dots {} and {}".format(dot2,p1))
                # print(edges[p1][dot2],edges[dot2][p1])
                edges[p1][dot2] = 1
                edges[dot2][p1] = 1
                check_squares()
                # print(original_squares,square_vals)
                if original_squares != square_vals:
                    print("SQUARE COMPLETE")
                    return 1
                return 2
        p1 += 1
        
    
    
    
def p2_move():
    global p2,m2
    p2 += m2
    while True:
        if p2 > 36:
            p2 -= 36
        p2_coord = num_to_coord(p2)
        options = p2_adj(p2_coord[0],p2_coord[1])
        print(options)
        original_squares = square_vals[:]
        for edge in options:
            x,y = edge
            dot2 = coord_to_num(x,y)
            # print(p1,dot2)
            if edges[p2][dot2] == False and edges[dot2][p2] == False:
                print("P2 connects dots {} and {}".format(dot2,p2))
                # print(edges[p1][dot2],edges[dot2][p1])
                edges[p2][dot2] = 
                edges[dot2][p2] = 2
                check_squares()
                if original_squares != square_vals:
                    print("SQUARE COMPLETE")
                    return 2
                return 1
        p2 += 1
        
    
        
# for y in range(6):
#     for x in range(6):
#         print(x,y)
#         print(p1_adj(x,y))
#         print(p2_adj(x,y))
        # print()
        # print(x,y)
        # print("NUM",coord_to_num(x,y))
        # print(num_to_coord(coord_to_num(x,y)))
# exit()
turn = 1
for _ in range(t):
    print(turn)
    if turn == 1:
        turn = p1_move()
    else:
        turn = p2_move()

    # for a in range(5):
    #     row = ''
    #     for b in range(5):
    #         row += square_vals[a*5+b] + " "
    #     print(row)
        


