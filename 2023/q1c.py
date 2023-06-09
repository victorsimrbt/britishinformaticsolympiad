import time
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
for i in range(1,100):
    fib_i = fib(i)
    if fib(i) > 5000000000:
        break
    usable_fibs.append(fib(i))
    
def check_path(path):
    path = sorted(path)
    if len(set(path)) != len(path):
        return False
    indexes = [usable_fibs.index(num) for num in path]
    
    for i in range(1,len(indexes)):
        if indexes[i]-indexes[i-1] == 1:
            return False
    return True
        
print("NAME: VICTOR SIM")
print("YEAR: 11")
print("SCHOOL: WICHESTER COLLEGE")
usable_fibs = usable_fibs
print(usable_fibs)
print(len(usable_fibs))
numbers = []

# print("NAME: VICTOR SIM")
# print("YEAR: 11")
# print("SCHOOL: WICHESTER COLLEGE")
# root = int(input())
# head = 0
# queue = [[root,[]]]
# time1 = time.time()
# while head < len(queue):
#     last = queue[head][0]
#     path = queue[head][1]
#     if last == 0:
#         if check_path(path):
#             print(" ".join([str(char) for char in path]))
#         break
#         # paths.append(path)
    
#     for fib in usable_fibs:
#         if fib > last:
#             break
#         leftover = last-fib
#         if not(leftover in visited):
#             queue.append([leftover,path+[fib]])
#             visited.add(leftover)
#     head += 1
# print(time.time()-time1)
        