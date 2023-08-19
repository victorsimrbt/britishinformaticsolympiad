import random
import time
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
from itertools import permutations
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

perms = list(permutations(alphabet,3))
for i in range(100):

    s1,s2 = ''.join(random.choice(perms)),''.join(random.choice(perms))
    print(s1,s2)
    if ispat(s1):
        print("YES")
    else:
        print("NO")
        
    if ispat(s2):
        print("YES")
    else:
        print("NO")
        
    if ispat(s1+s2):
        print("YES")
    else:
        print("NO")
    print()
    time.sleep(1)