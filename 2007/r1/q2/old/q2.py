import numpy as np
import copy

players = ["O","X"]

class Space:
    def __init__(self,status,idx):
        self.status = status
        self.adjacent = []
        self.idx = idx
    def check_move(self,player):
        if self.status == player:
            adjacent_open = [space.status == player for space in self.adjacent]
            if adjacent_open.count(True) == 2:
                return False
            else:
                return True
        return False

            
    
class Game:
    def __init__(self,layout):
        self.spaces = []
        for i in range(9):
            self.spaces.append(Space(layout[i],i))
        self.centre = self.spaces[0]
        self.centre.adjacent = self.spaces[1:]
        
        kawai = self.spaces[1:]
        for i in range(len(kawai)):
            kawai[i].adjacent.append(kawai[i-1])
            if i+1 != len(kawai):
                kawai[i].adjacent.append(kawai[i+1])
            else:
                kawai[i].adjacent.append(kawai[0])
            kawai[i].adjacent.append(self.centre)
    def print_status(self):
        print_string = ''
        for space in self.spaces:
            print_string += space.status
        return print_string
    
    def legal_moves(self,player):
        legal_moves = []
        for space in self.spaces:
            if space.check_move(player):
                #print([space.status for space in space.adjacent])
                new_moves = [[space.idx,new_space.idx] for new_space in space.adjacent if new_space.status == 'E']
                legal_moves += new_moves
        return legal_moves
    
    def make_move(self,move,player):
        start,end = move
        self.spaces[start].status = 'E'
        self.spaces[end].status = player
        
def choose_move(game,player):
    '''
    Use leftmost
    1. Move that will make the opponent lose
    2. Avoid moves that will allow the opponent to beat me
    3. Otherwise move the leftmost piece
    '''
    other_player = players[:]
    other_player.remove(player)
    legal_moves = game.legal_moves(player)
    
    #print(legal_moves)
    #print(other_player)
    for move in legal_moves:
        #print(move)
        game_copy = copy.deepcopy(game)
        game_copy.make_move(move,player)
        #print(game_copy.print_status())
        opp_legal = game_copy.legal_moves(other_player[0])
        #print(opp_legal)
        #print(game_copy.legal_moves("X"))
        #print("RULE 1: CHECKING FOR GAME ENDING MOVE")
        if not(opp_legal):
            return move
        
        for move in opp_legal:
            second_copy = copy.deepcopy(game_copy)
            if not(second_copy.legal_moves(player)):
                #print("RULE 2: MOVE RESULTS IN LOSS")
                pass
    #print("RULE 3: LEFTMOST MOVE")
    return legal_moves[0]

layout = input()
#layout = "EOOOOXXXX"
game = Game(layout)
turn = 0
while True:
    instruction = input()
    player = players[turn%2]
    if 'n' in instruction:
        #print(player)
       # print(game.legal_moves(player))
        if game.legal_moves(player):
            move = choose_move(game,player)
            game.make_move(move,player)
        else:
            print("Player {} wins".format(turn%2+2))
            print(game.print_status())
            break
        if game.legal_moves(player):
            move = choose_move(game,player)
            game.make_move(move,player)
        else:
            print("Player {} wins".format(turn%2+2))
            print(game.print_status())
            break
        print(game.print_status())
        turn += 1
    elif 'r' in instruction:
        while True:
            player = players[turn%2]
            if game.legal_moves(player):
                move = choose_move(game,player)
                game.make_move(move,player)
            else:
                print(player)
                print(game.print_status())
                break
            print(game.print_status())
            turn += 1