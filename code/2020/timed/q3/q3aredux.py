'''
num(length, num_last, last_char)

num(4,0,0) = num(3,1,A) + num(3,1,B)

num(3,1,A) = num(2,2,A) + num(2,1,B)

num(3,1,B) = num(2,1,A) + num(2,2,B)

num(2,2,A) = num(1,1,B) + num(1,3,A) 

num(1,1,B) = len(characters)
'''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

p,q,r = map(int,input().split())

dp = {}
def num(length,num_last,last_char):
    if num_last > q:
        return 0
    if length == 1:
        if num_last == q:
            return p-1
        else:
            return p
    if length == 0:
        return 0
        
    if tuple([length,num_last,last_char]) in dp:
        return dp[tuple([length,num_last,last_char])]
    else:
        ans = 0
        for i in range(p):
            if alphabet[i] == last_char:
                last = num_last + 1
            else:
                last = 1
            ans += num(length-1,last,alphabet[i])
        dp[tuple([length,num_last,last_char])] = ans
    return ans


num(r,0,0)
ans = ''
target = int(input())-1
length = r
num_last = 2
last_char = None

while length > 1:
    configs = 0
    prev = 0
    for char in alphabet[:p]:
        if char == last_char:
            last = num_last + 1
        else:
            last = 1
        prev = num(length-1,last,char)
        configs += prev
        if configs > target:
            ans += char
            target = target - (configs-prev)
            if char == last_char:
                num_last += 1
            else:
                num_last = 1
            last_char = char
            break
    length -= 1
    
for char in alphabet[target:p]:
    if char == last_char and num_last == q:
        pass
    else:
        ans += char
        break
print(ans)