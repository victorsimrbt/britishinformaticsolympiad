'''
531434
998284
'''
def shuffle(a,b,c,d,e,f):
    shuffle_to = [a,b,c,d,e,f]
    shuffled = []
    
    n = 1
    shuffle_idx = 0
    while len(shuffled) != 6:
        if n == shuffle_to[shuffle_idx]:
            shuffled.append(cards[0])
            shuffle_idx = (shuffle_idx+1)%6
            n = 0
            cards.pop(0)
        else:
            cards.append(cards.pop(0))
        n += 1
    return shuffled
configs = set()
for a in range(1,11):
    for b in range(1,11):
        for c in range(1,11):
            for d in range(1,11):
                for e in range(1,11):
                    for f in range(1,11):
                        cards = []
                        value = 'A23456789TJQK'
                        suits = 'CHSD'
                        for suit in suits:
                            for val in value:
                                cards.append(val+suit)
                        cards = shuffle(a,b,c,d,e,f)
                        configs.add(''.join(sorted(cards)))
print(len(configs))
# print(configs)
                        
                        