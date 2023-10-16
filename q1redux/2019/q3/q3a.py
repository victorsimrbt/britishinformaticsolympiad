'''

DCBA
DCAB
DBCA
DBAC
DACB

GFEDCBA

'''
import time
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
calls = 0
def valid(string):
    global calls
    calls += 1
    for a in range(len(string)-2):
        for b in range(a,len(string)):
            for c in range(b,len(string)):
                if string[a] < string[b] and string[b] < string[c]:
                    print
                    return False
    return True
        
memo = {}
def num_configs(string,remain):
    # print(string,remain)
    
    if (string,remain) in memo:
        print("RECALL")
        return memo[(string,remain)]
    else:
        if not(valid(string)):
            return 0 
        if remain == 0:
            # print(string)
            # exit()
            return 1
        ans = 0
        for char in alphabet:
            if not(char in string):
                ans += num_configs(string+char,remain-1)
        memo[(string,remain)] = ans
        return memo[(string,remain)]

# print(valid("ADB"))
l,p = input().split()
start = time.time()
l = int(l)
alphabet = alphabet[:l]
print(num_configs(p,l-len(p)))
# print(calls)
print(time.time()-start)
    