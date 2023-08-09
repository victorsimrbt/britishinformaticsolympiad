'''
RGBG
BRR
GR
B

RGGG
BGG
RG
B
'''
trials = 20

import random

convert = {
    "RB" : "G",
    "BR" : "G",
    "GB" : "R",
    "BG" : "R",
    "GR" : "B",
    "RG" : "B",
    "BB" : "B",
    "RR" : "R",
    "GG" : "G"
}

def next(row):
    if len(row) == 1:
        return row
    new_row = ''
    for i in range(len(row)-1):
        double = row[i] + row[i+1]
        new_row += convert[double]
    return new_row

for i in range(4,500):
    # i is row_len
    start = random.choice("RGB")
    end = random.choice("RGB")
    
    final = []
    for _ in range(trials):
        row = start
        for x in range(i-2):
            row += random.choice("RGB")
        row += end
        while True:
            row = next(row)
            if len(row) == 1:
                break
        final.append(row)
    if len(set(final)) == 1:
        print(i,final)
        
'''
10,28,82
'''

        