import numpy as np
class Space:
    def __init__(self,position,colour):
        self.position = position
        self.neighbours = []
        self.colour = colour
        
def adjacent_points(point):
    x,y = point
    adjacent = [[x-1,y],
                [x+1,y],
                [x,y-1],
                [x,y+1]]
    valid_adjacent = [point for point in adjacent if 3 >= point[0] >= 0 and 3 >= point[1] >= 0]
    return valid_adjacent

class Game:
    def __init__(self,config):
        self.board = []
        self.columns = [list(reversed([config[i][column] for i in range(4)])) for column in range(4)]
        self.column_counter = [0,0,0,0]
        for row in range(4):
            row_spaces = []
            for column in range(4):
                row_spaces.append(Space([row,column],config[row][column]))
            self.board.append(row_spaces)
        for row in range(4):
            for column in range(4):
                adj = adjacent_points([row,column])
                adj_points = [self.board[adj_point[0]][adj_point[1]] for adj_point in adj]
                self.board[row][column].neighbours = adj_points
    def print_board(self):
        for row in range(4):
            print_string = ''
            for column in range(4):
                print_string += self.board[row][column].colour
            print(print_string)
    def find_blocks(self):
        visited = []
        temp_cells = []
        self.disappear_cells = []
        def search(cell,score):
            global temp_cells
            #print(cell.position,score)
            if cell.position not in visited:
                visited.append(cell.position)
                neighbours = cell.neighbours
                for neighbour in neighbours:
                    if neighbour.colour == cell.colour and neighbour.position not in visited:
                        self.disappear_cells.append(neighbour.position)
                        score = search(neighbour,score+1)
                return score
        scores = []
        for row in range(4):
            for column in range(4):
                score = search(self.board[row][column],0)
                if score:
                    scores.append(score+1)
                    self.disappear_cells.append([row,column])
        #print(scores)
        final_score = [np.prod(scores) if scores else 0][0]
        return final_score

    def clear_blocks(self):
        for position in self.disappear_cells:
            self.board[position[0]][position[1]].colour = ' '
            
        for column in range(4):
            values = [self.board[i][column].colour for i in range(4)]
            #print(values,self.columns[column])
            remove_space = [value for value in values if value != ' ']
            while len(remove_space) < 4:
                remove_space.insert(0,self.columns[column][self.column_counter[column]%4])
                self.column_counter[column] += 1
            for i in range(4):
                self.board[i][column].colour = remove_space[i]
                
    def add_blocks(self):
        pass

print(np.prod([]))
board = []
for i in range(4):
    board.append(list(input()))
#board = [['R', 'R', 'G', 'B'], ['G', 'R', 'B', 'G'], ['R', 'R', 'G', 'B'], ['G', 'B', 'R', 'B']]
game = Game(board)
score = 0

while True:
    rounds = int(input())
    if rounds:
        for i in range(rounds):
            new_score = game.find_blocks()
            #print("NEW",new_score)
            if new_score == 0:
                print(score)
                print("GAME OVER")
                exit()
            score += new_score
            game.clear_blocks()
        game.print_board()
        print(score)
    else:
        break
    
