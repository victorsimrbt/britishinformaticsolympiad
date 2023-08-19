'''
get the number of zeros

1: 1111
2: 10111
3: 11011
4: 11101
5: 11110
6: 100111
7: 101011
8: 101101
9: 101110
10: 110011
11: 110101
12: 110110
13: 111001
14: 111010
15: 111100
16: 1000111
'''
import time
import math
from itertools import combinations, permutations

n,m = map(int,input().split())
ls = m

def num(zeros,ones):
    if zeros == 0:
        return 1
    if ones == 0:
        return 1
    return int(math.factorial(zeros+ones) / ((math.factorial(zeros)) * math.factorial(ones)))

def seperate(string):
    ans = ''
    for i in range(0,len(string),6):
        ans += string[i:i+6] + ' '
    return ans
        

# print([[''.join(val)] for val in set(list(permutations("10011")))])
# print(len([[''.join(val)] for val in set(list(permutations("10011")))]))
# print(num(2,3))
# exit()
zeros = 0
ones = ls-1
total_configs = 0
target = n
while True:
    # ! next char is zero?
    configs = num(zeros,ones)
    print(configs)
    if total_configs + configs >= target:
        target -= total_configs
        break
    total_configs += configs
    zeros += 1
    # ! next char is one?
    
print("{} ones, {} zeros".format(ones+1,zeros))
# print("Target: {}".format(target))
# exit()
# ones = 3
# zeros = 1
ans_len = ones+zeros
ans = ''
def solve(zeros,ones,target):
    global ans
    # print()
    # print("SOLVE",zeros,ones,target)
    covered = 0
    if len(ans) == ans_len:
        # print("DONE") '
        ans = '1'+ans
        print(seperate(ans))
        # new_ans = list(ans)
        # for i in range(len(ans))
        exit()
    
    if zeros > 0:
        next_zero = num(zeros-1,ones)
    else:
        next_zero = 0
        
    if ones > 0:
        next_one = num(zeros,ones-1)
    else:
        next_one = 0
    
    # next_one = num(zeros,ones-1)
    # print(next_zero,next_one)
    if next_zero >= target:
        ans += '0'
        # print("ZERO")
        solve(zeros-1,ones,target)
    elif next_zero + next_one >= target:
        ans += '1'
        # print("ONE")
        solve(zeros,ones-1,target-next_zero)

solve(zeros,ones,target)
print(ans)
        
    