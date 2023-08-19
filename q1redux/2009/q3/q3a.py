import time
dp = [0] * 33
s,n = map(int,input().split())

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

num(s)

target = n
ans = ''

while s > 0:
    total_configs = 0
    for block in range(1,10):
        configs = num(s-block)
        if (total_configs + configs) >= target:
            ans += str(block) + ' '
            if total_configs < target:
                target -= total_configs
            s -= block
            break
        total_configs += configs
print(ans)
