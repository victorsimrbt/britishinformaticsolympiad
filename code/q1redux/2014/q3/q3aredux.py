from math import comb

# print(comb(35, 2))
n = int(input())

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def build(n, targetLen, ans=""):
    # ! if reach target, end
    if targetLen == 0:
        return ans
    # ! start at "A" or the last character of the answer
    start = (alpha.index(ans[-1]) + 1) if ans else 0
    for letter in range(start, 36):
        # ! ways to choose remaining characters from characters following value
        can = comb(36 - (letter + 1), targetLen - 1)
        if can >= n:
            return build(n, targetLen - 1, ans + alpha[letter])
        n -= can


targLen = 1
# ! keep removing from target, so target becomes relative to the number of characters
while comb(36, targLen) < n:
    n -= comb(36, targLen)
    targLen += 1

print(build(n, targLen))