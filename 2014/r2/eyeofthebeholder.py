import random
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def testcase_gen(n):
    ans = ''
    for i in range(n//2):
        ans += random.choice(alphabet)
    
    if n % 2 == 0:
        ans = list(ans+''.join(list(reversed(ans))))
        random.shuffle(ans)
        return ''.join(ans)
    else:
        ans = list(ans + random.choice(alphabet) + ''.join(list(reversed(ans))))
        random.shuffle(ans)
        return ''.join(ans)

string = testcase_gen(2**16)
# string = input()
# string = "VMMVI"

print(string)
counts = {}
for term in string:
    if term in counts:
        counts[term] += 1
    else:
        counts[term] = 1
        
remaining = []
for key in sorted(counts.keys(),reverse = True):
    for i in range(counts[key]//2):
        remaining.append(key)
        
        
first_half = ''
for i in range(len(string)//2):
    # print(i)
    orig = string[i]
    l = 0
    r = len(remaining)-1
    target = orig
    # print(target)

    while l <= r:
        mid = (l+r)//2
        # print(l,r,mid)
        if remaining[mid] == target:
            # print("FOUND")
            break
        if remaining[mid] > target:
            l = mid + 1
        else:
            r = mid - 1
    if remaining[mid] == target:
        first_half += remaining[mid]
        remaining.pop(mid)
    else:
        first_half += remaining[mid-1]
        remaining.pop(mid-1)
    # print(remaining,mid)
    # if len(remaining) == 1:
    #     first_half += remaining[0]
    #     remaining.pop(0)
    # else:
    #     first_half += remaining[mid]
    #     remaining.pop(mid)
    

new_str = first_half
if len(string) % 2 == 1:
    mid = [key for key in counts if counts[key] %2 == 1][0]
    print(new_str+mid+''.join(list(reversed(new_str))))
else:
    print(new_str+''.join(list(reversed(new_str))))