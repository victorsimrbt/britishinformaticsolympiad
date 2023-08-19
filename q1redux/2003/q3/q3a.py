'''
since l is given, it is just sorting by magnitude

if i have n zeros and m ones, how many conmbinations

(n+m)! / ((n!) + m!)

abcd

1100

determine how many ones and zeros
and then determine which permutations


1111

10111
11011
11101
11110

11
101
110
1001
1010
'''
import time
import math
from itertools import combinations

# math.comb
# n,n = map(int,input().split())
n,m = map(int,input().split())
ls = m

def num(zeros,ones):
    return int(math.factorial(zeros+ones) / ((math.factorial(zeros)) * math.factorial(ones)))

zeros = 0
ones = ls-1
total_configs = 0
target = n-1
while True:
    # ! next char is zero?
    # print(zeros,ones,total_configs)
    configs = num(zeros,ones)
    if total_configs + configs > target:
        # print("WHAT",total_configs,configs)
        target -= total_configs
        break
    total_configs += configs
    zeros += 1
    # ! next char is one?
    
print("{} ones, {} zeros".format(ones+1,zeros))
# print(ones,zeros)

# ! find the nth permutation of x zeros and y ones
'''

'''

memo = {}
def configs(zeros,idx,length):
    '''
    how many ways to place n zeros from idx(exclusive)
    '''
    
    if zeros == 0:
        return 1
    
    if (zeros,idx,length) in memo:
        return memo[(zeros,idx,length)]
    else:
        ans = 0
        for i in range(1,length-idx+1):
            # print(idx+i)
            ans += configs(zeros-1,idx+i,length+1)
        memo[(zeros,idx,length)] = ans
    return memo[(zeros,idx,length)]
    
# print("WTF",configs(0,0,4))

# target = 2
ans = ["1" for i in range(ones+1)]
print(ans,target)
target += 1
prev = 0
while zeros > 0:
    total_ways = 0
    print("zeros from idx {}".format(prev))
    for idx in range(prev,ones+2):
        ways = configs(zeros-1,idx,ones+1)
        print((zeros-1,idx,ones+1),ways)
        print(total_ways)
        if ways + total_ways > target:
            prev = idx
            ans.insert(idx,"0")
            target = ways
            zeros -= 1
            break
        total_ways += ways
    time.sleep(1)
print(ans)
        

'''
'''
# configs = num(zeros,ones)
# print("TOTAL",configs)
# print("TARGET",target)
# if target >= configs/2:
#     ans += "1"
# else:
#     ans += "0"
# print(ans)
        
    


# print(num(2,2))