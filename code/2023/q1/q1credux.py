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
for i in range(1,53):
    fib_i = fib(i)
    usable_fibs.append(fib_i)

valid = 0
for i in range(3,52):
    value_1 = i
    for i_2 in range(1,i-1):
        value_2 = i_2
        for i_3 in range(1,i_2-1):
            valid += 1

print(usable_fibs,valid)