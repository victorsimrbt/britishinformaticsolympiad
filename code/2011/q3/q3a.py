import math
from itertools import permutations
ten_combos = [[i,10-i] for i in range(1,10)]
#print(ten_combos)

digits = 1

# Substract 1 from input target
target = int(input())-1

while True and digits < 100:
    if digits == 1:
        digit_size = 1
    else:
        digit_size = len(ten_combos)**(digits//2)
    if target >= digit_size:      
        target -= digit_size
    else:
        print("PARAMS",target,digit_size,digits)
        break
    digits += 1

def find_entry(digits,target):
    group = len(ten_combos) ** (digits//2)
    #print("GROUP SIZE", group)
    pairs = []
    search_value = target
    while True:
        chunk_size = group / 9
        if chunk_size < 1:
            break
        #print("CHUNK_SIZE AND SEARCH_VALUE",chunk_size,search_value)
        #print(int(search_value // chunk_size))
        pairs.append(ten_combos[int(search_value // chunk_size)])
        search_value = search_value % chunk_size
        group = chunk_size
    return pairs

def construct_string(digits,pairs):
    answer_list = [0]*(digits//2*2)
    print(pairs)
    for i in range(len(pairs)):
        answer_list[i] = pairs[i][0]
        answer_list[len(answer_list)-i-1]=pairs[i][1]
        #print(answer_list)
    #print(answer_list)
    if digits % 2 != 0:
        answer_list.insert(digits//2,5)
    answer_list = [str(term) for term in answer_list]
    return ''.join(answer_list)
        
pairs = find_entry(digits,target)
print(construct_string(digits,pairs))
