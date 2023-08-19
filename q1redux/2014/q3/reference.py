'''
num(length, num_last, last_char)

num(4,0,0) = num(3,1,A) + num(3,1,B)

num(3,1,A) = num(2,2,A) + num(2,1,B)

num(3,1,B) = num(2,1,A) + num(2,2,B)

num(2,2,A) = num(1,1,B) + num(1,3,A) 

num(1,1,B) = len(characters)
'''
import time
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

p,q,r = map(int,input().split())

dp = {}
def num(length,num_last,last_char):
    if num_last > q:
        print("WTF")
        return 0
    if length == 1:
        if num_last == q:
            return p-1
        else:
            return p
    if length == 0:
        if num_last >= q:
            return 1
        else:
            return 1
        
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
target = int(input())
# print(dp)
'''
def solve(state,target):
    if target == 0:
        exit()
    covered = 0
    for char in alphabet:
        if covered + dp[state] > target:
            solve(state,target-dp[state])
        covered += dp[state]
'''
def solve(state,target):
    global ans
    print()
    print("SOLVE",state,target)
    if len(ans) == r:
        print("DONE")
        print(ans)
        exit()
    # print(state,target)
    covered = 0
    for char in alphabet[:p]:
        length,num_last,last_char = state
        if char == last_char:
            new_state = [length-1,num_last + 1,last_char]
        else:
            new_state = [length-1,1,char]
        subtree_size = num(new_state[0],new_state[1],new_state[2])
        print(new_state,(subtree_size+covered)-target)
        if covered + subtree_size >= target:
            print(covered,subtree_size,target)
            ans += char
            print(ans,target,covered+subtree_size)
            if subtree_size <= target:
                # print("WHAT")
                solve(new_state,target-covered)
            else:
                solve(new_state,target)
            break
        covered += subtree_size
        # time.sleep(1)

solve((r,0,0),target)