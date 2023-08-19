import math
import time

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
    
    # while True:
    #     neighbor = num - pow(2,power)
    #     if neighbor <= 0:
    #         break
    #     if not neighbor in dist and isprime(neighbor):
    #         neighbors.append(neighbor)
    #         dist[neighbor] = distance + 1
    #     power += 1

    # power = 0
    while True:
        neighbor = num + pow(2,power)
        if neighbor > l:
            break
        if not neighbor in dist and isprime(neighbor):
            neighbors.append(neighbor)
            dist[neighbor] = distance + 1
        power += 1
    return neighbors
        
l,p,q = map(int,input().split())

# print(gen_neighbor(2,100,13))
# print(isprime(4))
# exit()
start = time.time()
queue = [p]
dist[p] = 1
head = 0
while head < len(queue):
    last = queue[head]
    neighbors = gen_neighbor(last,l,dist[last])
    # print(last,neighbors)
    if q in neighbors:
        print(dist[q])
        print(time.time()-start)
        exit()
    queue += neighbors
    head += 1
print(time.time()-start)
# print(gen_neighbor(293,l))


