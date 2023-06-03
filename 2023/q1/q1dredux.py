memo = {}
visited = set()
def fib(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    ans = fib(n-1) + fib(n-2)
    memo[n] = ans
    return ans

usable_fibs = []
for i in range(1,49):
    fib_i = fib(i)
    usable_fibs.append(fib_i)

relevant = usable_fibs[42:]
print(relevant)
print(relevant[3]+relevant[1])
print(5000000000-relevant[-2])
print(192473024+4807526976)
ans = relevant[2]-relevant[1] + relevant[0] + (relevant[4]-relevant[3] - (relevant[2]-relevant[1])) + (5000000000-relevant[4] - (relevant[2]-relevant[1]))
print(ans)