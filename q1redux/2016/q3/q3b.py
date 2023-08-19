'''
65
'''
import time
import math

memo = {}
def isprime(n):
    if n in memo:
        return memo[n]
    else:
        for f in range(2,int(math.sqrt(n))+1):
            if n % f == 0:
                memo[n] = False
                return memo[n]
        memo[n] = True
    return memo[n]

dist = {}
def gen_neighbor(num,l,distance):
    power = 0
    neighbors = []
    
    while True:
        neighbor = num - pow(2,power)
        if neighbor <= 0:
            break
        if isprime(neighbor):
            neighbors.append(neighbor)
            dist[neighbor] = distance + 1
        power += 1

    power = 0
    while True:
        neighbor = num + pow(2,power)
        if neighbor > l:
            break
        if isprime(neighbor):
            neighbors.append(neighbor)
            dist[neighbor] = distance + 1
        power += 1
    return neighbors
        
# for i in range(1,20):
#     if isprime(i):
#         print(i,gen_neighbor(i,20,0))
# exit()
l,p,q = map(int,input().split())

# print(gen_neighbor(2,100,13))
# print(isprime(4))
# exit()
queue = [[p,[p]]]
head = 0
ans = 0
tings = set()
while head < len(queue):
    last,path = queue[head]
    neighbors = gen_neighbor(last,l,0)
    for neighbor in neighbors:
        if neighbor == q:
            print(sorted(path+[neighbor]))
            tings.add(tuple(sorted(path+[neighbor])))
            ans += 1
        else:
            if not(neighbor) in path:
                queue.append([neighbor,path+[neighbor]])
    head += 1
    # time.sleep(1)
print(ans,len(tings))
# print(gen_neighbor(293,l))


