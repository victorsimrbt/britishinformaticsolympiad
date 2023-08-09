'''
['A', 'A', 'B', 'C', 'B', 'A', 'A'] (1)
['A', 'A', 'BCB', 'A', 'A'] (1)
['A', 'ABCBA', 'A'] (1)
['AA', 'B', 'C', 'B', 'AA'] (1)
['AA', 'BCB', 'AA'] (1)
''' 
import time
groupings = []
def generate_groupings(string):
    if len(string) == 1:
        # print(string)
        return [[string]]
    if len(string) == 0:
        return [[]]
    
    total = []
    for i in range(len(string)):
        block1 = string[:i+1]
        groupings = generate_groupings(string[i+1:])
        # print(block1,groupings)
        if not(groupings):
            groupings = [[block1]]
        else:
            # print(groupings)
            for i in range(len(groupings)):
                groupings[i].insert(0,block1)
        total += groupings
    # print(string,groupings)
    return total

groupings = generate_groupings(input())
# print(groupings)
ans = 0
for group in groupings:
    if list(reversed(group)) == group and not(len(group) == 1):
        ans += 1
        print(group)
print(ans)