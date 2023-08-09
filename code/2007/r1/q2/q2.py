game_states = set()
players = ["O","X"]

def adj(marker_idx):
    if marker_idx == 0:
        return [idx for idx in range(1,9)]
    if marker_idx == 1:
        return [2,8]
    if marker_idx == 8:
        return [1,7]
    return [marker_idx+1,marker_idx-1]
def move(marker_idx,board):
    board = list(board)
    empty_idx = board.index("E")
    
    adjacent_markers = [board[val] for val in adj(marker_idx)]
    if (empty_idx in adj(marker_idx) or empty_idx == 0) and (adjacent_markers.count(board[marker_idx]) < 2 or marker_idx == 0):
        board[empty_idx] = board[marker_idx]
        board[marker_idx] = "E"
        return ''.join(board)
    return False

def legal_moves(board,char):
    boards = []
    for i in range(9):
        if board[i] == char:
            config = move(i,board)
            if config != False:
                boards.append(config)
    return boards

def get_result(board,char):
    if not(legal_moves(board,char)):
        return False
    return True

def get_move(orig_board,char):
    can_lose = False
    player = char
    next_char = [val for val in players if val != player][0]
    for next_board in legal_moves(orig_board,char):
        if get_result(next_board,next_char) == False:
            return next_board
        next_next_board = legal_moves(next_board,next_char)
        if can_lose:
            return next_board
        for board in next_next_board:
            if get_result(board,char) == False:
                can_lose = True
    return legal_moves(orig_board,char)[0]
    
turn = 0
board = input()
while True:
    command = input()
    if command == "n":
        if get_result(board,players[turn%2]) == False:
            print("Player {} wins".format(2-turn%2))
            break
        board = get_move(board,players[turn%2])
        game_states.add(board)
        turn += 1
        print(board)
    if get_result(board,players[turn%2]) == False:
        print("Player {} wins".format(2-turn%2))
        break
    elif command == "r":
        while True:
            if get_result(board,players[turn%2]) == False:
                print(board)
                print("Player {} wins".format(2-turn%2))
                exit()
            board = get_move(board,players[turn%2])
            if board in game_states:
                print("Draw")
                exit()
            game_states.add(board)
            turn += 1