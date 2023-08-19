'''
 E O
O X X
O   X
 O X
 
XEOXXXOOO
1. XOOXXXOOE
2. XOEXXXOOO

XOOXXXOOE will be played
'''

board = "EOOOOXXXX"

def adj(idx):
    left = idx+1
    right = idx-1
    if idx == 0:
        return [i for i in range(1,len(board))]
    if idx == 1:
        return [0,len(board)-1,2]
    if idx == len(board)-1:
        return [0,1,7]
    return [0,left,right]

def generate_legal_moves(board,player):
    legal = []
    for from_sq in range(len(board)):
        for to_sq in range(len(board)):
            adjacent = adj(from_sq)
            if board[from_sq] == player and to_sq in adjacent and board[to_sq] == "E":
                if from_sq != 0:
                    score = 0
                    for square in adjacent[1:]:
                        if board[square] == player:
                            score += 1
                    if score == 2:
                        pass
                    else:
                        legal.append([from_sq,to_sq])
                else:
                    legal.append([from_sq,to_sq])
    return legal

def result(board,player):
    # is game over
    if not(generate_legal_moves(board,player)):
        return True
    else:
        return False

def play_move(move,board):
    board = list(board)
    from_sq,to_sq = move
    board[to_sq] = board[from_sq]
    board[from_sq] = "E"
    return board

def play(board,player,other_player):
    can_lose = False
    legal_moves = generate_legal_moves(board,player)
    for move in legal_moves:  
        new_board = play_move(move,board)
        if result(new_board,other_player):
            # print("Rule 1")
            return move
        
        for opp_move in generate_legal_moves(new_board,other_player):
            new_new_board = play_move(opp_move,new_board)
            if not(result(new_new_board,player)):
                # print("Rule 2")
                can_lose = True
                
    
    if can_lose:
        for move in generate_legal_moves(board,player):
            potential_loss = False
            new_board = play_move(move,board)
            
            for opp_move in generate_legal_moves(new_board,other_player):
                new_new_board = play_move(opp_move,new_board)
                if result(new_new_board,player):
                    potential_loss = True
            
            if not(potential_loss):
                return move
    # print("Rule 3")
    return legal_moves[0]


print(generate_legal_moves("XEOXXXOOO","O"))
print(play("XEOXXXOOO","O","X"))
# exit()
            
# print(new_board)
# print(result(new_board,"X"))


