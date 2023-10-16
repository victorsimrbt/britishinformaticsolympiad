'''
17 minutes
remember that "9" < "A"
'''
import math
import time
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
n = int(input())

# for n in range(1000):
    # inpt = n
length = 1
total_configs = 0
while True:
    configs_for_length = math.comb(len(alphabet),length)
    if total_configs + configs_for_length >= n:
        n -= total_configs
        # ! length is set
        break
    total_configs += configs_for_length
    length += 1
    
# print(length,n)
ans = ''
while len(ans) != length:
    total_configs = 0
    for i in range(len(alphabet)):
        if not(ans) or i > alphabet.index(ans[-1]):
            configs_for_char = math.comb(len(alphabet)-i-1,length-len(ans)-1)
            # print(alphabet[i],configs_for_char,total_configs)
            if total_configs + configs_for_char >= n:
                n -= total_configs
                ans += alphabet[i]
                # print("ADDED {}, N is {}".format(alphabet[i],n))
                break
            total_configs += configs_for_char
# time.sleep(0.1)
print(ans)

'''
abc = def

abc/d = ef
'''