'''
2, 11, 3, 10, 4 then 9

'2C', 'KC', '3H', 'KH', '4S', 'KS', '2D', 'KD', '4C', '2H', '7H', '5S'
'''
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

print(shuffle(2,11,3,10,4,9))