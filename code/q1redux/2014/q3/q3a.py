
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
dp = {}
def num_configs(length,last_char):
    if length == 0:
        return 1
    if length < 0:
        return 0
    if tuple([length,last_char]) in dp:
        return dp[tuple([length,last_char])]
    else:
        ans = 0
        for i in range(last_char,len(characters)):
            ans += num_configs(length-1,i)
        dp[tuple([length,last_char])] = ans
        return dp[tuple([length,last_char])]


# print(num_configs(10,0))
        
n = int(input())
chars = 1
total_configs = 0
    
    
while True:
    configs = num_configs(chars,0)
    if total_configs + configs >= n:
        # print(total_configs,configs)
        n -= total_configs
        break
    total_configs += configs
    chars += 1
    
    

# print("{} characters needed".format(chars))

    
total_chars = chars
ans = ''
last_idx = -1

def solve(target,chars):
    global ans
    global last_idx
    # print("SOLVE",ans,target,chars)
    if len(ans) == total_chars:
        # print("WHAT?")
        print(ans)
        exit()
    total_configs = 0
    for char_idx in range(last_idx+1,len(characters)):
        configs = num_configs(chars,char_idx+1)
        # print("CHAR",chars,characters[char_idx],total_configs,configs)
        # print("TARGET",target)
        if total_configs + configs >= target:
            ans += characters[char_idx]
            last_idx = char_idx
            target -= total_configs
            solve(target,chars-1)
        total_configs += configs
# print("Target is {}".format(n))
solve(n,chars-1)