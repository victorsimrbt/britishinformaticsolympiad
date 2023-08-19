'''
no as that would mean there would infinitely travel path in differnet ways
heading is arbitrary, simply rotation of board
each square can only be accessed four ways
the square will be updated and when accessed from the same direction will have the same 
'''

dice = [6,1,2,5,3,4]
heading = 0

# ! dont use star notation!!
grid = [[1 for i in range(11)] for i in range(11)]

def down(dice,pos):
    x,y = pos
    bottom,top,up,down,left,right = dice
    return [down,up,bottom,top,left,right],[x,y+1]

def up(dice,pos):
    x,y = pos
    bottom,top,up,down,left,right = dice
    return [up,down,top,bottom,left,right],[x,y-1]

def left(dice,pos):
    x,y = pos
    bottom,top,up,down,left,right = dice
    return [left,right,up,down,top,bottom],[x-1,y]

def right(dice,pos):
    x,y = pos
    bottom,top,up,down,left,right = dice
    return [right,left,up,down,bottom,top],[x+1,y]

print(down(dice,[0,0]))
print(up(dice,[0,0]))
print(left(dice,[0,0]))
print(right(dice,[0,0]))