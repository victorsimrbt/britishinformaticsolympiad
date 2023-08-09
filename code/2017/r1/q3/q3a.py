'''
p is the number of parcels
i is the max weight of the objects
n is the total number of items across all packages
w is the weight of each parcels

generate all possible parcels:
    generate all the ways in which 1 to n-1 objects can make up w 

    match it up with all and if not same, double. add it up

kindof easy
'''
import numpy as np
p,i,n,w = map(int,input().split())

max_items = n-p+1

parcels = set()
parcels_of_len = [0 for i in range(26)]
visited = set()
def generate_parcels(remain_w,config):
    if len(config) > (n-p+1):
        return
    if remain_w == 0:
        parcels.add(tuple(sorted(config)))
        parcels_of_len[len(config)] += 1
        return
    for first_w in range(1,i+1):
        if first_w <= remain_w:
            new_config = config + [str(first_w)]
            if tuple(sorted(new_config)) in visited:
                pass
            else:
                visited.add(tuple(sorted(new_config)))
                generate_parcels(remain_w-first_w,new_config)

ans = 0      

def count_ways(n_left,way):
    '''
    number of ways to make n with the numbers
    for each of those ways, multiply the probabilities
    '''
    # print(n_left,way)
    global ans
    if n_left == 0 and len(way) == p:
        # ways.append(way)
        ans += np.prod(way)
        return
    if n_left < 0 or len(way) > p:
        return
    valid = [a for a in range(len(parcels_of_len)) if parcels_of_len[a] > 0]
    for val in valid:
        count_ways(n_left - val,way + [parcels_of_len[val]])
        
generate_parcels(w,[])
count_ways(n,[])
print(ans)
'''
count number of ways that parcels can be matched
'''