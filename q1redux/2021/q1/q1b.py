'''
BDCA
CBDA
CDAB
DACB
DBAC
'''
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
perms = permutations("ABCD")
for perm in perms:
    if ispat(''.join(perm)):
        print(''.join(perm))