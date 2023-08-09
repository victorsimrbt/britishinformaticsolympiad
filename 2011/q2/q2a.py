import time
cards = []
value = 'A23456789TJQK'
suits = 'CHSD'
for suit in suits:
    for val in value:
        cards.append(val+suit)
# print(cards)

def shuffle(a,b,c,d,e,f):
    shuffle_to = [a,b,c,d,e,f]
    shuffled = []
    
    n = 1
    shuffle_idx = 0
    while len(shuffled) != 52:
        if n == shuffle_to[shuffle_idx]:
            shuffled.append(cards[0])
            shuffle_idx = (shuffle_idx+1)%6
            n = 0
            cards.pop(0)
        else:
            cards.append(cards.pop(0))
        n += 1
    return shuffled

def strategy_1(piles):
    # ! (top_card,size)
    for i in range(len(piles)-1,0,-1):
        current = piles[i]
        adjacent = piles[i-1]
        # print(current[0],adjacent[0],current[1],adjacent[1])
        if current[0][0] == adjacent[0][0] or current[0][1] == adjacent[0][1]:
            # print("current")
            return (i,i-1)
        if i -3 >= 0:
            separated = piles[i-3]
            if current[0][0] == separated[0][0] or current[0][1] == separated[0][1]:
                # print("adjacent")
                return (i,i-3)
    return False

def strategy_2(piles):
    moves = []
    for i in range(len(piles)-1,0,-1):
        current = piles[i]
        adjacent = piles[i-1]
        # print(current[0],adjacent[0],current[1],adjacent[1])
        if current[0][0] == adjacent[0][0] or current[0][1] == adjacent[0][1]:
            size = current[1] + adjacent[1]
            moves.append([size,i,True,(i,i-1)])
        if i -3 >= 0:
            separated = piles[i-3]
            if current[0][0] == separated[0][0] or current[0][1] == separated[0][1]:
                size = current[1] +  separated[1]
                moves.append([size,i,False,(i,i-3)])
    moves.sort(reverse = True)
    if moves:
        return moves[0][-1]
    else:
        return False
    
def legal_moves(piles):
    legal_moves = 0
    for i in range(len(piles)-1,0,-1):
        current = piles[i]
        adjacent = piles[i-1]
        # print(current[0],adjacent[0],current[1],adjacent[1])
        if current[0][0] == adjacent[0][0] or current[0][1] == adjacent[0][1]:
            legal_moves += 1
        if i -3 >= 0:
            separated = piles[i-3]
            if current[0][0] == separated[0][0] or current[0][1] == separated[0][1]:
                legal_moves += 1
    return legal_moves
    
    
def strategy_3(piles):
    moves = []
    for i in range(len(piles)-1,0,-1):
        current = piles[i]
        adjacent = piles[i-1]
        # print(current[0],adjacent[0],current[1],adjacent[1])
        if current[0][0] == adjacent[0][0] or current[0][1] == adjacent[0][1]:
            piles_copy = [pile[:] for pile in piles]
            piles_copy = play_move(piles_copy,(i,i-1))
            score = legal_moves(piles_copy)
            moves.append([score,i,True,(i,i-1)])
        if i -3 >= 0:
            separated = piles[i-3]
            if current[0][0] == separated[0][0] or current[0][1] == separated[0][1]:
                piles_copy = [pile[:] for pile in piles]
                piles_copy = play_move(piles_copy,(i,i-3))
                score = legal_moves(piles_copy)
                moves.append([score,i,True,(i,i-3)])
    moves.sort(reverse = True)
    if moves:
        return moves[0][-1]
    else:
        return False
    
    

def play_move(piles,move):
    from_pile,to_pile = move
    piles[to_pile][0] = piles[from_pile][0]
    piles[to_pile][1] += piles[from_pile][1]
    piles.pop(from_pile)
    return piles
    
        
a,b,c,d,e,f = map(int,input().split())
shuffled = shuffle(a,b,c,d,e,f)
print(shuffled[0],shuffled[-1])
piles = [[card,1] for card in shuffled]
# print(shuffled)
while True:
    if len(piles) == 1:
        print(len(piles),piles[0][0])
        break
    move = strategy_1(piles)
    # print(piles[move[0]][0],piles[move[1]][0])
    if move:
        piles = play_move(piles,move)
    else:
        print(len(piles),piles[0][0])
        break
    # print(piles)
    
for suit in suits:
    for val in value:
        cards.append(val+suit)
shuffled = shuffle(a,b,c,d,e,f)
piles = [[card,1] for card in shuffled]

while True:
    if len(piles) == 1:
        print(len(piles),piles[0][0])
        break
    move = strategy_2(piles)
    # print(piles[move[0]][0],piles[move[1]][0])
    if move:
        piles = play_move(piles,move)
    else:
        print(len(piles),piles[0][0])
        break
    
for suit in suits:
    for val in value:
        cards.append(val+suit)
        
        
shuffled = shuffle(a,b,c,d,e,f)
piles = [[card,1] for card in shuffled]

while True:
    if len(piles) == 1:
        print(len(piles),piles[0][0])
        break
    move = strategy_3(piles)
    # print(piles[move[0]][0],piles[move[1]][0])
    if move:
        piles = play_move(piles,move)
    else:
        print(len(piles),piles[0][0])
        break
# print(move)
# print(play_move(piles,move))
# while True
        
        
