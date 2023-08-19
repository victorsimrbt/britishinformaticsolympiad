'''
B (ACDEFGHIJKLMNOPQRSTUVWXYZ) permutations

B + pat of length 24 + A
no other possiblities as no more characters can be added

pat of length 24 containing not A or B
23 + 1 (C)
22 + 2 (CD)


pat of length 4

ABCD



three others + smallest
two others + two smallest

pats of length 3:
26*25 

pats of length 2:
26*25

pats of length 1:
26

def num_pats():



ABC
but must start with B

B
'''
def num_pats(n):
    # ! returns number of pats of length n
from itertools import permutations
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def ispat(string):
    if len(string) == 1:
        return True
    
    for split in range(1,len(string)):
        left = string[:split]
        right = string[split:]
        
        alphabetical = True
        for char1 in left:
            for char2 in right:
                if alphabet.index(char1) > alphabet.index(char2):
                    pass
                else:
                    alphabetical = False
        
        if alphabetical:
            # print(left,right)
            if ispat(''.join(reversed(left))) and ispat(''.join(reversed(right))):
                return True
        
        # print(left,right)
    return False
perms = permutations("ACDEFGHIJKLMNOPQRSTUVWXYZ")
for perm in perms:
    print("B"+''.join(perm))
    if ispat("B"+''.join(perm)):
        print(")0000000000000000000000000000000000000000")
        print(''.join(perm))