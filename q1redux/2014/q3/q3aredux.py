import math 
import time
memo = {}

def num_configs(last_char,length):
    # ! or just math.comb
    if length == 1:
        return 36-last_char
    if length <= 0:
        return 1
    if (last_char,length) in memo:
        return memo[(last_char,length)]
    else:
        ans = 0
        for char in range(last_char+1,37):
            ans += num_configs(char,length-1)
        memo[(last_char,length)] = ans
        return memo[(last_char,length)]
    # ! the number of combinations 
# exit()
length = 1
target = int(input())
covered = 0
while True:
    if num_configs(0,length) + covered >= target:
        target -= covered
        break
    covered += num_configs(0,length)
    length += 1
    
ans = ''
last_char = 0
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ans_len = length
while len(ans) != ans_len:
    covered = 0
    for char in range(last_char+1,37):
        if covered + num_configs(char,length-1) >= target:
            ans += alpha[char-1]
            target -= covered
            last_char = char
            length -= 1
            break
        covered += num_configs(char,length-1)
print(ans)
