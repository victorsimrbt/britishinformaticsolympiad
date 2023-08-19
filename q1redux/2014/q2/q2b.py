'''
31
'''
# ! red is O, green is X, both is B
tile1 = [" O ",
         "X X",
         " O "]

tile2 = [" X ",
         "O O",
         " X "]

tile3 = [" O ",
         "O X",
         " X "]

tile4 = [" O ",
         "X O",
         " X "]

tile5 = [" X ",
         "X O",
         " O "]

tile6 = [" X ",
         "O X",
         " O "]

tile_strs = [0,tile1,tile2,tile3,tile4,tile5,tile6]

# n = int(input())
# tiles = []
# for i in range(n):
#     row = []
#     for val in list(map(int,input().split())):
#         row.append(tile_strs[val])
#     tiles.append(row)
    
'''
check if two tiles are adjacent
'''

def adj_tiles(x,y,player):
    # ! UP,RIGHT,DOWN,LEFT
    adjacent = [
        [x-1,y],
        [x,y+1],
        [x+1,y],
        [x,y-1]
    ]
    adj_tiles = [tl if (tl[0] >= 0 and tl[0] < len(tiles) and tl[1] >= 0 and tl[1] < len(tiles)) else None for tl in adjacent]
    
    # adjacent_tiles
    u,r,d,l = adj_tiles
    # print("URDL",u,r,d,l)
    real_adj = []
    if u and tiles[u[0]][u[1]][2][1] == tiles[x][y][0][1] == player:
        # print("U")
        # print(tiles[u[0]][u[1]],tiles[x][y])
        real_adj.append(u)
    if r and tiles[r[0]][r[1]][1][0] == tiles[x][y][1][2] == player:
        # print("R")
        # print(tiles[r[0]][r[1]],tiles[x][y])
        real_adj.append(r)
    if d and tiles[d[0]][d[1]][0][1] == tiles[x][y][2][1] == player:
        # print("D")
        # print(tiles[d[0]][d[1]],tiles[x][y])
        real_adj.append(d)
    if l and tiles[l[0]][l[1]][1][2] == tiles[x][y][1][0] == player:
        # print("L")
        # print(tiles[l[0]][l[1]],tiles[x][y])
        real_adj.append(l)
    return real_adj

def find_loop(x,y,player):
    score = 0
    # visited = set()
    paths = []
    queue = [[x,y,[[x,y]]]]
    orig_x = x
    orig_y = y
    head = 0
    while head < len(queue):
        x,y,path = queue[head]
        for neighbor_tile in adj_tiles(x,y,player):
            # if x == 1 and y == 1:
            #     print(neighbor_tile[0])
            if neighbor_tile[0] == orig_x and neighbor_tile[1] == orig_y and len(path) >= 4:
                # score += len(path)
                # print("WHAT")
                if not sorted(path) in paths:
                    paths.append(sorted(path))
            if not neighbor_tile in path:
                # visited.add(tuple(neighbor_tile))
                n_x,n_y = neighbor_tile
                new_node = [n_x,n_y,path+[neighbor_tile]]
                queue.append(new_node)
        # print(queue)
        head += 1
        # print(queue[-1])
        # print()
    return paths
tile_idx = [[1,3,4,1],
        [5,2,6,4],
        [4,2,3,5],
        [4,4,5,4]]
ans = 0
for r in range(4):
    for c in range(4):
        for new in range(1,7):
            if new != tile_idx[r][c]:
                tile_idx = [[1,3,4,1],
                        [5,2,6,4],
                        [4,2,3,5],
                        [4,4,5,4]]
                # print(r,c,new)
                tile_idx[r][c] = new
                # print(tile_idx)
                tiles = []
                for i in range(4):
                    row = []
                    for j in range(4):
                        row.append(tile_strs[tile_idx[i][j]])
                    tiles.append(row)

                # tiles[r][c] == i
                # print(adj_tiles(1,1,"O"))
                r_score = 0
                g_score = 0

                r_checked_paths = []
                g_checked_paths = []
                for x in range(len(tiles)):
                    for y in range(len(tiles)):
                        # print(x,y)
                        # print("ANS",adj_tiles(x,y,"O"))
                        paths = find_loop(x,y,"O")
                        for path in paths:
                            if not sorted(path) in r_checked_paths:
                                r_checked_paths.append(sorted(path))
                                r_score += len(path)
                        paths = find_loop(x,y,"X")
                        for path in paths:
                            if not sorted(path) in g_checked_paths:
                                g_checked_paths.append(sorted(path))
                                g_score += len(path)
                # print(r_score,g_score)
                if not(r_score > g_score):
                    print("SCORES",r_score,g_score)
                    print("WOOOOOOOAH",r,c,new)
                    ans += 1
                # print(r_score,g_score)
print(ans)