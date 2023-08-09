import numpy as np
import copy
markers = ['.','F','S','*']
p1_pos = [[0,0],[1,0],[2,0],[3,0],[4,0]]
p2_pos = [[0,4],[1,4],[2,4],[3,4],[4,4]]
neutron_pos = [2,2]
board = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]

for pos in p1_pos:
    board[pos[0]][pos[1]] = 1
    
for pos in p2_pos:
    board[pos[0]][pos[1]] = 2

board[2][2] = 3
# print(board)
def print_board(board):
    board = np.transpose(board)
    for a in range(4,-1,-1):
        print_string = ''
        for b in range(5):
            #print(a,b)
            print_string += markers[board[a][b]]
        print(print_string)

def legal_moves(position,board):
    positions = []
    modifiers = [[0,1],[1,1],
                [1,0],[1,-1],
                [0,-1],[-1,-1],
                [-1,0],[-1,1]]
    
    for mod in modifiers:
        pos = position[:]
        while pos[0] <= 4 and pos[1] <= 4 and pos[0] >=0 and pos[1] >= 0:
            pos[0] += mod[0]
            pos[1] += mod[1]
            if pos[0] > 4 or pos[1] > 4 or pos[0] < 0 or pos[1] < 0:
                pos[0] -= mod[0]
                pos[1] -= mod[1]
                positions.append(pos)
                break
            if board[pos[0]][pos[1]] != 0:
                pos[0] -= mod[0]
                pos[1] -= mod[1]
                positions.append(pos)
                break
    positions = [pos for pos in positions if pos != position]
    return positions

def play_move(from_,to,board):
    bd = copy.deepcopy(board)
    temp = bd[from_[0]][from_[1]]
    bd[to[0]][to[1]] = temp
    bd[from_[0]][from_[1]] = 0
    return bd

def play(turn,piece_pos,board):
    if turn == 1:
        positions = p1_pos
    else:
        positions = p2_pos
    win_y = [None,0,4]
    opp = 3- turn
    for a in range(5):
        for b in range(5):
            if board[a][b] == 3:
                neutron_coord = [a,b]
                break
    legal_positions = legal_moves(neutron_coord,board)
    if not(legal_positions):
        print_board(board)
        exit()
    # print_board(board)
    rule_2 = True
    rule_3_board = None
    rule_2_board = None
    for position in legal_positions:
        bd = play_move(neutron_coord,position,board[:])
        # print_board(bd)
        if position[1] == win_y[turn]:
            print("Rule 1")
            print_board(bd)
            exit()
            return bd
        if position[1] != win_y[opp] and rule_2:
            rule_2 = False
            rule_2_board = bd
        if position[1] != win_y[turn] and position[1] != win_y[opp]:
            rule_3_board = bd
            legal_positions = legal_moves(piece_pos,rule_3_board)
            if legal_positions:
                print("Rule 3")
                # print(legal_positions)
                # print(positions)
                piece = positions.index(piece_pos)
                positions[piece] = legal_positions[0]
                rule_3_board = play_move(piece_pos,legal_positions[0],rule_3_board)
                return rule_3_board
    if rule_2:
        print("Rule 2")
        print_board(play_move(neutron_coord,legal_positions[0],board[:]))
        exit()
        return rule_2_board


player_1 = [int(char) for char in input().split()]
player_2 = [int(char) for char in input().split()]

p1_counter = 0
p2_counter = 0

turn = 1
board = play(1,p1_pos[player_1[p1_counter % 5]-1],board)
print_board(board)
p1_counter += 1
# print(legal_moves([2,3],board))
# print(p2_pos)
board = play(2,p2_pos[player_2[p2_counter % 5]-1],board)
print_board(board)
p2_counter += 1

while True:
    board = play(1,p1_pos[player_1[p1_counter % 5]-1],board)
    print(1)
    print_board(board)
    p1_counter += 1
    # print(legal_moves([2,3],board))
    board = play(2,p2_pos[player_2[p2_counter % 5]-1],board)
    print(2)
    print_board(board)
    p2_counter += 1


'''
establish squares
establish markers

p1_pos = [(x,y for each piece)]

def legal_moves(position,board):
    positions = []
    modifiers = [[0,1],[1,1],
                [1,0],[1,-1],
                [0,-1],[-1,-1],
                [-1,0],[-1,1]]
    
    for mod in modifiers:
        pos = position
        while pos[0] <= 4 and pos[1] <= 4:
            pos[0] += mod[0]
            pos[1] += mod[1]
            if board[pos[0],pos[1]] != 0:
                pos[0] -= mod[0]
                pos[1] -= mod[1]
                positions.append(pos)
                break
    return positions
    
# def result(board,turn,piece_pos):
#     opp = 3-turn
#     win_y = [None,0,4]
#     neutron_coord = [[a,b] for a in range(5) if board[a,b] = 3] for b in range(5)]
#     if neutron_coord[1] == win_y[1]:
#         return 1
#     elif neutron_coord[1] == win_y[2]:
#         return 2
    
#     if len(set(legal_moves(neutron_coord,board))) == 1:
#         return opp
    
#     if len(set(legal_moves(piece_pos,board))) == 1:
#         return opp
#     return None

def play_move(from,to,board):
    temp = board[from[0]][from[1]]
    board[to[0]][to[1]] = temp
    board[from[0]][from[1]] = 0
    return board
    
def play(turn,piece_pos,board):
    opp = 3- player
    neutron_coord = [[a,b] for a in range(5) if board[a,b] = 3] for b in range(5)]
    legal_positions = legal_moves(neutron_coord,board)
    rule_2 = True
    rule_3_board = None
    rule_2_board = None
    for position in legal_positions:
        board = play_move(neutron_coord,position,board)
        if position[1] == win_y[turn]:
            board[neutron_coord[0]][neutron_coord[1]] = 0
            board[position[0]][position[1]] = 3
            return board
        if position[1] != win_y[opp] and not(rule_2_board):
            rule_2 = False
            rule_2_board = play_move(neutron_coord,position,board)
        if position[1] != win_y[turn] and position[1] != y_opp and not(rule_3_board):
            rule_3_board = play_move(neutron_coord,position,board)
    
    if rule_2:
        return rule_2_board
    else:
        legal_positions = legal_moves(piece_pos,board)
        play_move(piece_pos,legal_positions[0],rule_3_board)
        
player_1 = [int(char) for char in input().split()]
player_2 = [int(char) for char in input().split()]  

def print_board(board):
    for a in range(5):
        print_string = ''
        for b in range(5):
            print_string += board[a][b] + ' '
        print(print_string)
        
    
    
        
        
        
'''