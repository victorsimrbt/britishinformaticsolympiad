import math
'''
1 2 7 9 10
'''

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

for num1 in range(1,11):
    for num2 in range(num1,11):
        for num3 in range(num2,11):
            for num4 in range(num3,11):
                for num5 in range(num4,11):
                    sum15 = set()
                    cards = [num1,num2,num3,num4,num5]
                    sumto(cards,15,[])
                    if identical(cards) + len(sum15) == 0:
                        print(cards)