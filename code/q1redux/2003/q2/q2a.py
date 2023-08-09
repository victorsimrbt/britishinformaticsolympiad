import time as sleepy

p = int(input())

schedule = []
for i in range(p):
    x,y,t = map(int,input().split())
    # ! schedule instance: length,centre,inc,time
    schedule.append([0,[x,y],1,t])
    schedule.append([0,[x,y],-1,t+2])
banks = list(map(int,input().split()))
# banks = [-100,100]
t = int(input())

river = {}
# banks = [-100,100]
# banks = [-100,10]
for x in range(-4,5):
    for y in range(-4,5):
        river[(x,y)] = 0
        
def print_grid(grid):
    for y in reversed(range(-4,5)):
        row = ''
        for x in range(-4,5):
            # print(x,y)
            if x in banks:
                row += "X"
            else:
                if grid[(x,y)] < 0:
                    row += "O"
                if grid[(x,y)] == 0:
                    row += "-"
                if grid[(x,y)] > 0:
                    row += "*"
        print(row)
        
def diamond(length,centre):
    if length == 0:
        return [centre]
    '''
    ---*---
    --*-*--
    -*-o-*-
    --*-*--
    ---*---
    centre (0,0)
    clockwise:
        (0,-2)
        (1,-1)
        (2, 0)
        (1, 1)
    they are all n units away from the centre
    '''
    pts = []
    for x_dist in range(length):
        # ! positive version
        new_pt = centre[:]
        new_pt[0] += x_dist
        new_pt[1] += (length-x_dist)
        pts.append(new_pt)
        
        new_pt = centre[:]
        new_pt[0] -= x_dist
        new_pt[1] -= (length-x_dist)
        pts.append(new_pt)
    
    for y_dist in range(length):
        # ! positive version
        new_pt = centre[:]
        new_pt[1] += y_dist
        new_pt[0] -= (length-y_dist)
        pts.append(new_pt)
        
        new_pt = centre[:]
        new_pt[1] -= y_dist
        new_pt[0] += (length-y_dist)
        pts.append(new_pt)
    pts = [tuple(pt) for pt in pts]
    return pts

def update(points,inc,grid,centre_x):
    for point in points:
        x,y = point
        for bank in banks:
            if x >= bank and centre_x < bank:
                # print("MAX",x,max(banks),max(banks) - (x-max(banks)) - 1)
                x = bank - (x-bank) - 1
            elif x <= bank and centre_x > bank:
                # print("MIN",x,min(banks),min(banks) + (min(banks)-x))
                # ! how far past bank + bank
                x = bank + (bank-x) + 1
                
        point = (x,y)
        if point in grid:
            grid[point] += inc
        else:
            grid[point] = inc
        # print(point,grid[point])
    return grid

# def drop_pebble(point,t):
#     schedule.append([point,t])

# ! schedule instance: length,centre,inc,time

# schedule = [[0,[-1,0],1,1],
#             [0,[-1,0],-1,3],
#             [0,[2,0],1,2],
#             [0,[2,0],-1,4]]

def schedule_t(schedule,t):
    new_schedule = []
    for wave in schedule:
        length,centre,inc,time = wave
        if t > time:
            new_schedule.append([t-time,centre,inc,t])
        else:
            new_schedule.append([length,centre,inc,time])
    return new_schedule
            

# t = 5
# print(schedule)
schedule = schedule_t(schedule,t)
print(schedule)
river = {}
for x in range(-4,5):
    for y in range(-4,5):
        river[(x,y)] = 0
new_schedule = []
for i in range(len(schedule)):
    length,centre,inc,time = schedule[i]
    if t == time:
        pts = diamond(length,centre) 
        # print(len(pts))
        river = update(pts,inc,river,centre[0])
print_grid(river)


# for t in range(1,6):
#     river = {}
#     for x in range(-4,5):
#         for y in range(-4,5):
#             river[(x,y)] = 0
#     new_schedule = []
#     for i in range(len(schedule)):
#         length,centre,inc,time = schedule[i]
#         if t == time:
#             pts = diamond(length,centre) 
#             river = update(pts,inc,river)
#             new_schedule.append([length+1,centre,inc,time+1])
#         # print(t,schedule[i])
#         if time > t:
#             new_schedule.append(schedule[i])
#     schedule = new_schedule
#     # print(t)
#     # for ting in schedule:
#     #     print(ting)
#     # print(t)
#     print_grid(river)
#     print()
#     # sleepy.sleep(1)
#     # print(t)
# # print(schedule == new)
    
    
# pts = diamond(0,[0,0]) 
# print(pts)
# river = update(pts,1,river)
# # river[(0,1)] = 1
# print_grid(river)

'''
X              X
X              X
X              X
'''