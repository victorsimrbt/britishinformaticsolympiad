'''
let L be lucky number array
outputs:
    if input is L[n]:
        return L[n] -1 , L[n] + 1
    if input is between L[n] and L[n] + 1:
        return L[n] and L[n] + 1
        
        
there are 
1, 3, 5

1 2 3 4 5
1 3 5 7 9

a b c d

1999999998
'''

# ! how many lucky numbers between and X?
# ! one is the first lucky number (1), which is smaller than 2
ans = 0
lucky_nums = 1000000000 - 1
ans += lucky_nums

# ! how many inter-lucky number gaps are there
# ! lucky numbers - 1
ans += lucky_nums - 1
# ! for 2
ans += 1


print(ans)

