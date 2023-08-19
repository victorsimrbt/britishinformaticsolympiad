import math
cards = list(map(int,input().split()))

def identical(cards):
    score = 0
    counts = {}
    for card in cards:
        if not card in counts:
            counts[card] = 1
        else:
            counts[card] += 1
    
    for card in counts:
        score += math.comb(counts[card],2)
    return score

sum15 = set()
def sumto(cards,target,seq):
    if target < 0:
        return False
    if target == 0:
        sum15.add(tuple(sorted(seq)))
        return seq
    for i in range(len(cards)):
        if not i in seq:
            card = cards[i]
            sumto(cards,target-card,seq+[i])
    return

sumto(cards,15,[])
print(identical(cards)+len(sum15))
    
    