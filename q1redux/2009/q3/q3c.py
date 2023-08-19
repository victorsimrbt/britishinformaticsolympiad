'''
last numerical is first dictionary (1)
it is the first entry listed dictionary, it is all 1s 
it will have most number of digits
but since all characters are 1, it will be the first listed dictionarily

last entry in dictionary is first numbered numerically
smallest number of digits so first 

'''
import time
dp = [0] * 51
# s,n = map(int,input().split())
def num(total):
    # print(total)
    if total == 0:
        return 1
    if dp[total]:
        return dp[total]
    else:
        ans = 0
        for i in range(1,10):
            if i <= total:
                ans += num(total-i)
        dp[total] = ans
    return dp[total]

val = 8
num(val//2)
# ! ODD NUMBER, WITH I IN THE MIDDLE
total = 0
for i in range(1,10):
    if (val - i) % 2 == 0:
        total += num((val-i)//2)
total += num(val//2)
print(total)
    

