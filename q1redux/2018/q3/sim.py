'''
Full solution:
first determine the increasing subsequences of p of length 1 & 2 with the smallest tail (a & b)
Let R be the remaining letters to be placed after p.
For example if l = 8 and p = 'ECHG', R is {A,B,D,F}
​
Divide R into 3 segments, left, mid and right with:
left: the number of letters smaller than a
mid: the number of letters larger than a but smaller than b
right: the number of letters larger than b
​
The problem count(length, left, mid, right) can be solved recursively with a transition formula.
We would be placing letters from left to right one by one.
left + mid + right is always the total number of remaining letters to be placed.
'''
# return (a, b). a: smallest letter; b: end of the increasing subsequence of length 2 with the smallest tail, if it exists
# this function returns a tuple with only 1 element if there is no increasing subsequence of length 2

memo = {}
def scan(p):
    q = [p[0]]
    for i in range(1, len(p)):
        if p[i] < q[0]:
            q[0] = p[i]
        elif len(q) == 1:
            q.append(p[i])
        else:
            q[1] = p[i]
    return tuple(q)

def count(length, left, mid, right):
    if left + mid + right == 0: 
        return 1
    ans = 0
    if (length,left,mid,right) in memo:
        return memo[(length,left,mid,right)]
    else:
        if length == 1:
            for i in range(left):
                ans += count(1, i, 0, right + left - i - 1)
            for i in range(right):
                ans += count(2, left, i, right-i-1)
        else:
            for i in range(left):
                ans += count(2, i, mid+left-i-1, right)
            for i in range(mid):
                ans += count(2, left, i, right+mid-i-1)
        memo[(length,left,mid,right)] = ans
        return ans

line = input().split()
l = int(line[0])
p = line[1]
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
remainder = set(letters[:l]) - set(p)
q = scan(p)
left, mid, right = 0, 0, 0
for ch in remainder:
    if ch < q[0]:
        left += 1
    elif len(q) > 1 and ch < q[1]:
        mid += 1
    else:
        right += 1

print(count(len(q), left, mid, right))