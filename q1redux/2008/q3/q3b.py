'''
1. 15
2. 571
'''
def op1(shirts):
    return shirts[1:4]+shirts[0]+shirts[4:]

def op2(shirts):
    return shirts[:3]+shirts[-1]+shirts[3:-1]

def op3(shirts):
    return shirts[3]+shirts[:3]+shirts[4:]

def op4(shirts):
    return shirts[:3]+shirts[4:]+shirts[3]

shirts = ["1234567"]
for i in range(6):
    new_shirts = []
    for shirt in shirts:
        new_shirts.append(op1(shirt))
        new_shirts.append(op2(shirt))
        new_shirts.append(op3(shirt))
        new_shirts.append(op4(shirt))
    shirts = new_shirts[:]
    
new_shirts = set(new_shirts)
print(len(new_shirts))
    