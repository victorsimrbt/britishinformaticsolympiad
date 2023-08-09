'''
221256270138418389602
'''
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
    
ans = 0
for i in range(1,37):
    ans += num_configs(36,0)