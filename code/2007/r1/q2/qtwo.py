
markers = ["E","O","X"]
board = "EOOOOXXXX"
board = input()
# board = "OXEOOXXXO"

def adjacent(space):
    # ! Checked
    if space == 0:
        adjacent = [1,2,3,4,5,6,7,8]
    elif space == 8:
        adjacent = [0,1,7]
    elif space == 1:
        adjacent = [0,2,8]
    else:
        adjacent = [0,space-1,space+1]
    adjacent = sorted(adjacent)
    return adjacent

# for i in range(9):
#     print(i,":",adjacent(i))

def legal_moves(player,board):
    # ! checked
    legal = []
    empty = board.index("E")
    neighbors = adjacent(empty)
    
    for space in neighbors:
        if board[space] == markers[player]:
            adjacent_markers = [board[adj] for adj in adjacent(space) if adj != 0]
            #print(space,adjacent_markers)
            if not(adjacent_markers.count(markers[player]) == 2) or space == 0:
                legal.append(space)
    return legal

def play_move(move,board,player):
    board = list(board)
    empty = board.index("E")
    board[empty] = markers[player]
    board[move] = "E"
    return ''.join(board)

def pick_move(player,board):
    opp = 3-player
    for move in legal_moves(player,board):
        #print(move)
        player_move = play_move(move,board,player)
        #print(move,player_move)
        if not(legal_moves(opp,player_move)):
            #print("Rule 1")
            return move
    for move in legal_moves(player,board):
        player_move = play_move(move,board,player)
        playable = True
        for opp_move in legal_moves(opp,player_move):
            opponent_move = play_move(opp_move,player_move,opp)#
            #print(opponent_move)
            if not(legal_moves(player,opponent_move)):
                playable = False
                break
        if playable:
            #print("Rule 2")
            return move
    #print("Rule 3")
    return legal_moves(player,board)[0]

# print(legal_moves(2,"OXOEOXXXO"))
# print()
# print(legal_moves(1,"EXOOOXXXO"))
print(pick_move(1,"OOEXOOXXX"))

turn = 1
while True:
    order = input()
    if order == "n":
        if not(legal_moves(turn,board)):
            print(board)
            print("Player {} wins".format(3-turn))
            exit()
        move = pick_move(turn,board)
        board = play_move(move,board,turn)
        turn = 3-turn
        print(board)
        if not(legal_moves(turn,board)):
            print(board)
            print("Player {} wins".format(3-turn))
            exit()
    elif order == "r":
        states = []
        while True:
            #print(board,turn)
            if not(legal_moves(turn,board)):
                print(board)
                print("Player {} wins".format(3-turn))
                exit()
            move = pick_move(turn,board)
            board = play_move(move,board,turn)
            if board in states:
                #print(board)
                print("Draw")
                exit()
            states.append(board)
            turn = 3-turn
            
        
print(legal_moves(1,board))
print(pick_move(1,board))

'''
establish spaces
assign adjacent spaces to each space

assign markers to each space

markers = ["E","O","X"]
def adjacent(space):
    if space == 0:
        adjacent = [1,2,3,4,5,6,7,8]
    elif space == 8:
        adjacent = [0,7]
    else:
        adjacent = [space-1,space+1]
    return adjacent

def legal_moves(player,board):
    legal = []
    empty = board.index("E")
    neighbors = adjacent(empty)
    
    for space in neighbors:
        if board[space] == player and [board[i] for i in adjacent(space)].count("player") != len(adjacent(space)):
            legal.append(space)
    return legal
def play_move(move,board,player):
    empty = board.index("E")
    board[empty] = markers[player]
    board[move] = "E"
    return board
            

def pick_move(player,board):
    opp = 3-player
    for move in legal_moves(player,board) (left to rihgt):
        player_move = play_move(move,board)
        if not(legal_moves(opp,board)):
            return move
        for move in legal_moves(opp,new_board):
            opponent_move= play_move(move,player_move)
            if legal_moves(player,board):
                return move
    return legal_moves(player,board)[0]
                
            
'''