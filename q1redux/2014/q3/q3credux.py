import math
ans = 0
for i in range(1,36):
    ans += math.comb(36,i)
print(ans)