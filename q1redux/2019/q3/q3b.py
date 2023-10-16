'''
BOI
IBO
IOB
OBI
OIB
'''
import itertools

def valid(string):
    # global calls
    # calls += 1
    for a in range(len(string)-2):
        for b in range(a,len(string)):
            for c in range(b,len(string)):
                if string[a] < string[b] and string[b] < string[c]:
                    # print
                    return False
    return True

configs = itertools.permutations("DCBA")
for config in configs:
    if valid(''.join(config)):
        print(''.join(config))
        
'''
DCBA


DCBA

DCAB
DACB
ADCB

DBCA
BDCA

DBAC
DACB
CDBA
CDAB
CBDA
CBAD
CADB
BDAC
BADC
'''