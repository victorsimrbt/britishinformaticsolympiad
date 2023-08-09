'''
bottom: 6
top: 1

up: 2
down: 5

left: 3
right: 4

28
232
'''

# ! order: bottom,top,up,down,left,right
pos = [5,5]
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

orig = dice[:]
pos = [0,0]
ans = 0
directions = [up,right,down,left]
for tip1 in directions:
    for tip2 in directions:
        for tip3 in directions:
            for tip4 in directions:
                for tip5 in directions:
                    for tip6 in directions:
                        pos = [0,0]
                        dice = dice = [6,1,2,5,3,4]
                        dice,pos = tip1(dice,pos)
                        dice,pos = tip2(dice,pos)
                        dice,pos = tip3(dice,pos)
                        dice,pos = tip4(dice,pos)
                        dice,pos = tip5(dice,pos)
                        dice,pos = tip6(dice,pos)
                        if pos == [0,0] and dice[0] != 6:
                            print(tip1.__name__,
                                tip2.__name__,
                                tip3.__name__,
                                tip4.__name__,
                                tip5.__name__,
                                tip6.__name__)
                            ans += 1
                # print(pos,dice)
print(ans)

'''
pairs:
L R
R L 
U D
D U

4*4*4
'''


# def print_grid(grid,centre):
#     start_x,start_y = centre
#     for y_inc in range(-1,2):
#         ans = ''
#         for x_inc in range(-1,2):
#             # print(start_x+x_inc,start_y + y_inc,grid[start_x+x_inc][start_y+y_inc])
#             x,y = start_x+x_inc,start_y+y_inc
#             if x >= 0 and x < 11 and y >= 0 and y < 11:
#                 ans += str(grid[x][y])
#             else:
#                 ans += "X"
#         print(ans)
        
# def whole(grid):
#     for y in range(11):
#         row = ''
#         for x in range(11):
#             row += str(grid[x][y])
#         print(row)
        
# def clock(direction_idx):
#     if direction_idx != 3:
#         return direction_idx + 1
#     else:
#         return 0
#     # ! up down left right

# def anticlock(direction_idx):
#     if direction_idx != 0:
#         return direction_idx -1
#     else:
#         return 3
        

        
# def move(grid,pos,dice,heading):
#     num = dice[1] + grid[pos[0]][pos[1]]
#     if num > 6:
#         num -= 6
        
#     # print("POSITION,num",grid[pos[0]][pos[1]],num)
#     # print("HEADING",directions[heading])
#     grid[pos[0]][pos[1]] = num
#     # print("UPDATE",pos[0],pos[1],num)
#     # print(num == 2)
#     if num == 1 or num == 6:
#         new_dice,new_pos = directions[heading](dice,pos)
#         return grid,new_pos,new_dice,heading
#     elif num == 2:
#         new_dice,new_pos = directions[clock(heading)](dice,pos)
#         heading = clock(heading)
#         return grid,new_pos,new_dice,heading
#     elif num == 3 or num == 4:
#         new_dice,new_pos = directions[clock(clock(heading))](dice,pos)
#         heading = clock(clock(heading))
#         return grid,new_pos,new_dice,heading
#     elif num == 5:
#         new_dice,new_pos = directions[anticlock(heading)](dice,pos)
#         heading = anticlock(heading)
#         return grid,new_pos,new_dice,heading
        
        
        
# # print(directions[clock(1)])
# # print(directions[clock(clock(1))])
# # exit()
# # print(grid)
# # print(grid[4][5])
# start_x,start_y = 5,5
# for y_inc in range(-1,2):
#     row = input().split()
#     idx = 0
#     for x_inc in range(-1,2):
#         # print("ROW",row[idx])
#         grid[start_x+x_inc][start_y + y_inc] = int(row[idx])
#         idx += 1


# # pos = [5,5]
# # heading = 0
# # for i in range(5):
# #     # print(pos,dice,directions[heading])
# #     grid,pos,dice,heading = move(grid,pos,dice,heading)
# #     if pos[0] < 0:
# #         pos[0] = 10
# #     if pos[0] >= 11:
# #         pos[0] = 0 
        
# #     if pos[1] < 0:
# #         pos[1] = 10
# #     if pos[1] >= 11:
# #         pos[1] = 0 
# #     print_grid(grid,[5,5])
# # exit()
# # print()
# pos = [5,5]
# heading = 0
# while True:
#     n = int(input())
#     if n == 0:
#         exit()
#     for i in range(n):
#         grid,pos,dice,heading = move(grid,pos,dice,heading)
#         if pos[0] < 0:
#             pos[0] = 10
#         if pos[0] >= 11:
#             pos[0] = 0 
            
#         if pos[1] < 0:
#             pos[1] = 10
#         if pos[1] >= 11:
#             pos[1] = 0 
#         # print(pos,dice,directions[heading])
#     print_grid(grid,pos)
#     # print()



# # for y in range(11):
# #     row = ''
# #     for x in range(11):
# #         row += str(grid[x][y])
# #     print(row)
# # for i in range(3):
    

# # print(down(dice))
# # print(up(dice))
# # print(left(dice))
# # print(right(dice))
