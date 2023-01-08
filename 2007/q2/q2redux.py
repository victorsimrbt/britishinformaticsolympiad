class Space:
    def __init__(self):
        self.adjacent = []
        self.marker = "E"
        self.idx = None
        
counter = 0
turns = ["O","X"] 
turn = "O"

other_turn = {
    "O" : "X",
    "X" : "O"
}

class Board:
    def __init__(self):
        self.spaces = []
        self.putahi = Space()
        self.putahi.idx = 1
        for i in range(4):
            space = Space()
            space.marker = "O"
            space.idx = 2+i
            self.spaces.append(space)
        for i in range(4):
            space = Space()
            space.marker = "X"
            space.idx = 6+i
            self.spaces.append(space)
        self.putahi.adjacent = self.spaces[:]
        for i in range(1,len(self.spaces)-1):
            self.spaces[i].adjacent = [self.spaces[i+1],self.spaces[i-1],self.putahi]
        self.spaces.insert(0,self.putahi)
        self.spaces[1].adjacent = [self.spaces[2],self.spaces[-1],self.putahi]
        self.spaces[-1].adjacent = [self.spaces[1],self.spaces[-2],self.putahi]
        
    def print_board(self):
        print_string = ''
        for space in self.spaces:
            print_string += space.marker
        return print_string
    
    def legal_moves(self,turn):
        legal_moves = []
        for from_space in self.spaces:
            adjacent_markers = [space.marker for space in from_space.adjacent]
            print(from_space.idx,adjacent_markers)
            if from_space.marker == turn and adjacent_markers.count(turn) != 2:
                for to_space in from_space.adjacent:
                    if to_space.marker == "E":
                        legal_moves.append([from_space.idx,to_space.idx])
        return legal_moves
    
    def play_move(self,move):
        from_space,to_space = move
        from_marker,to_marker = self.spaces[from_space - 1].marker,self.spaces[to_space - 1].marker
        self.spaces[from_space - 1].marker = "E"
        self.spaces[to_space - 1].marker = from_marker
    
    def make_move(self,turn):
        original_layout = [space.marker for space in self.spaces]
        legal_moves = self.legal_moves(turn)
        # Rule 1
        final_move = legal_moves[0]
        for move in legal_moves:
            #print(board.print_board())
            self.play_move(move)
            legal_moves = self.legal_moves(other_turn[turn])
           # for space in self.spaces:
                #print(space.marker)
            #print(legal_moves)
            # Rule 3
            if (not(legal_moves)):
                final_move = move
                return final_move
            #print("BOARD1")
            #print(board.print_board())
            for opp_move in legal_moves:
                self.play_move(opp_move)
                legal_moves = self.legal_moves(turn)
                if legal_moves:
                    final_move = move
                    board.assert_layout(original_layout)
                    return final_move
                    #return move
            #print("BOARD2")
            #print(board.print_board())
            board.assert_layout(original_layout)
            #print("")
        return final_move

    def assert_layout(self,string):
        for i in range(len(self.spaces)):
            self.spaces[i].marker = string[i]
        
            
                
board = Board()

starting_layout = input()
board.assert_layout(starting_layout)
print([space.idx for space in board.spaces[-1].adjacent])
print(board.spaces[1].idx,board.spaces[1].marker)
print(board.legal_moves("X"))
move = board.make_move("X")
board.play_move(move)
print(board.print_board())
# while True:
#     order = input()
#     if order == "n":
#         print(board.print_board())
#         if (not(board.legal_moves(turn))):
#             if turn == "O":
#                 print("Player 2 wins")
#             else:
#                 print("Player 1 wins")
#             exit(0)
#         print(board.legal_moves(turn))
#         move = board.make_move(turn)
#         board.play_move(move)
#         print(move)
#         print(board.print_board())
#         turn = other_turn[turn]
#     elif order == "r":
#         while True:
#             if (not(board.legal_moves(turn))):
#                 print(board.print_board())
#                 exit(0)
#             move = board.make_move(turn)
#             board.play_move(move)
#             print(move)
#             print(board.print_board())
#             turn = other_turn[turn]

            