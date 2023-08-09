'''
32 1 blocks
16 2 blocks
10 3 blocks
8 4 blocks
6 5 blocks
5 6 blocks
4 7 blocks
4 8 blocks
3 9 blocks

88
'''
total = 0
for i in range(1,10):
    total += 32//i
    print(32//i)
print(total)