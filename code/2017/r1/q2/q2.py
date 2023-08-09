edges = [[0]*36 for _ in range(36)]
markers = ['*','X','O']
squares = []
for left in range(30):
	if ((left+1) % 6 != 0 or left == 0):
 		squares.append([left,left+1,left+7,left+6,0])
# print(squares)

def set_edge(pt1, pt2):
	edges[pt1][pt2] = 1
	edges[pt2][pt1] = 1

def neighbors_clock(dot):
	ans = []
	if (dot >= 6):
		ans.append(dot - 6)
	if (dot % 6 != 5):
		ans.append(dot+1)
	if (dot < 30):
		ans.append(dot + 6)
	if (dot % 6 != 0 and dot != 0):
		ans.append(dot-1)
	return ans

def neighbors_anti(dot):
	ans = []
	if (dot >= 6):
		ans.append(dot - 6)
	if (dot % 6 != 0 and dot != 0):
		ans.append(dot-1)
	if (dot < 30):
		ans.append(dot + 6)
	if (dot % 6 != 5):
		ans.append(dot+1)
	return ans

# for i in range(36):
# 	print(neighbors(i))

def play(player, pos, mod):
    # make sure next_player is set correctly before return
    next_player = 3-player
    pos = (pos + mod) % 36
    
    while True:
        #print(pts,pos)			
        if player == 2:
            pts = neighbors_anti(pos)
        else:			
            pts = neighbors_clock(pos)						
        for pt in pts:
            if not(edges[pos][pt]):
                edges[pos][pt] = 1
                edges[pt][pos] = 1
                for square in squares:
                    if (edges[square[0]][square[1]] and 
                            edges[square[1]][square[2]]and
                            edges[square[2]][square[3]] and
                            edges[square[3]][square[0]] and square[4] == 0):
                        # print("SQUARE",square)
                        next_player = player
                        square[4] = player
                print(player,"EDGE",pos,pt)
                return pos, next_player
        pos = (pos+1)%36
        # print("increment")

def print_edges():
	print('set edges: ')
	for pt1 in range(36):
		for pt2 in range(36):
			if edges[pt1][pt2]:
				print(pt1,pt2, end='; ')
	print()

def print_squares():
	print('set squares: ')
	for i in range(25):
		if squares[i][4] != 0:
			print(i, end=' ')
	print()
				
# set_edge(7,8)
# set_edge(8,9)
# set_edge(8,2)
# set_edge(7,13)
# set_edge(8,14)
# set_edge(9,15)
# # set_edge(14,15)
# set_edge(22,23)
# set_edge(22,28)
# set_edge(23,29)
# set_edge(29,35)
# set_edge(35,34)
# set_edge(34,28)

# print(play(1,0,14))
# p1,m1,p2,m2,t = 0, 14, 35, 15, 4
# turn = 2
# print_edges()
# print_squares()
# for i in range(t):
# 	#print(i+1,turn,p1+1,p2+1)
# 	if turn == 1:
# 			p1, turn = play(1, p1, m1)	
# 	else:
# 			p2, turn = play(2, p2, m2)
# 	print_edges()
# 	print_squares()
		

p1,m1,p2,m2,t = [int(val) for val in input().split()]
p1 -= 1
p2 -= 1
turn = 1
for i in range(t):
    #print(i+1,turn,p1+1,p2+1)
    if turn == 1:
        p1, turn = play(1, p1, m1)	
    else:
        p2, turn = play(2, p2, m2)
        
for i in range(5):
    print_string = ''
    for x in range(5):
        print_string += markers[squares[i*5+x][4]] + ' '
    print(print_string)

p1_squares = [square for square in squares if square[4] == 1]
p2_squares = [square for square in squares if square[4] == 2]
print(len(p1_squares),len(p2_squares))

# original sets
# set_edge(7,8)
# set_edge(8,9)
# set_edge(7,13)
# set_edge(8,14)
# set_edge(9,15)
# # set_edge(14,15)
# set_edge(22,23)
# set_edge(22,28)
# set_edge(23,29)
# set_edge(29,35)
# set_edge(35,34)
# set_edge(34,28)
