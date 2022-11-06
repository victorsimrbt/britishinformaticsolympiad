import numpy as np

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pos_dict = {
    UP : [-1,0],
    RIGHT : [0,1],
    DOWN : [1,0],
    LEFT : [0,-1]}

def clockwise(direction):
    new_direction = direction + 1
    if new_direction > 3:
        new_direction -= 4
    return new_direction

def anticlockwise(direction):
    new_direction = direction - 1
    if new_direction < 0:
        new_direction += 4
    return new_direction

def opposite(direction):
    new_direction = direction + 2
    if new_direction > 3:
        new_direction -= 4
    return new_direction

class Dice:
    def __init__(self):
        self.top = 1
        self.bottom = 6
        self.left = 3
        self.right = 4
        self.front = 2
        self.back = 5
        self.position = [5,5]
        self.heading = UP
        self.move_dict = {
            UP: self.up_turn,
            DOWN: self.down_turn,
            LEFT: self.left_turn,
            RIGHT: self.right_turn}
        
    def left_turn(self):
        top,bottom,left,right,front,back = self.top,self.bottom,self.left,self.right,self.front,self.back
        self.top = right
        self.bottom = left
        self.left = top
        self.right = bottom
        self.front = front
        self.back = back
        
    def right_turn(self):
        top,bottom,left,right,front,back = self.top,self.bottom,self.left,self.right,self.front,self.back
        self.top = left
        self.bottom = right
        self.left = bottom
        self.right = top
        self.front = front
        self.back = back
        
    def up_turn(self):
        top,bottom,left,right,front,back = self.top,self.bottom,self.left,self.right,self.front,self.back
        self.top = back
        self.bottom = front
        self.left = left
        self.right = right
        self.front = top
        self.back = bottom
        
    def down_turn(self):
        top,bottom,left,right,front,back = self.top,self.bottom,self.left,self.right,self.front,self.back
        self.top = front
        self.bottom = back
        self.left = left
        self.right = right
        self.front = bottom
        self.back = top
    
    def move(self,board):
        new_value = board[self.position[0]][self.position[1]] + self.top
        if new_value > 6:
            new_value -= 6
        board[self.position[0]][self.position[1]] = new_value
        if new_value == 1 or new_value == 6:
            new_direction = self.heading
            
        if new_value == 2:
            new_direction = clockwise(self.heading)
            
        if new_value == 3 or new_value == 4:
            new_direction = opposite(self.heading)
            
        if new_value == 5:
            new_direction = anticlockwise(self.heading)
            
        self.move_dict[new_direction]()
        self.position += np.array(pos_dict[new_direction])
        if self.position[0] > 10:
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = 10
        if self.position[1] > 10:
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = 10
        self.heading = new_direction
            

board = np.ones((11,11))
board[4][4],board[4][5],board[4][6] = [int(value) for value in input().split()]
board[5][4],board[5][5],board[5][6] = [int(value) for value in input().split()]
board[6][4],board[6][5],board[6][6] = [int(value) for value in input().split()]

def print_board(board,position):
    x,y = position
    row_1 = [[x-1,y-1],[x-1,y],[x-1,y+1]]
    row_2 = [[x,y-1],[x,y],[x,y+1]]
    row_3 = [[x+1,y-1],[x+1,y],[x+1,y+1]]
    row_1 = [str(int(board[value[0]][value[1]])) if 0 <= value[0] <= 10 and 0 <= value[1] <= 10 else "X" for value in row_1]
    row_2 = [str(int(board[value[0]][value[1]])) if 0 <= value[0] <= 10 and 0 <= value[1] <= 10 else "X" for value in row_2]
    row_3 = [str(int(board[value[0]][value[1]])) if 0 <= value[0] <= 10 and 0 <= value[1] <= 10 else "X" for value in row_3]
    
    print(' '.join(row_1))
    print(' '.join(row_2))
    print(' '.join(row_3))
    
    
dice = Dice()
while True:
    moves = int(input())
    if moves:
        for _ in range(moves):
            dice.move(board)
        print_board(board,dice.position)
    else:
        break
    #print(dice.top,dice.heading,dice.position)
    #print(board)

