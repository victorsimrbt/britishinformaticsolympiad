import math 
a,b,c,d,n = map(int,input().split())

def num_configs(counts):
    # counts = [string.count(char) for char in set(string)]
    divide = 1
    for count in counts:
        divide *= math.factorial(count)
    return int(math.factorial(sum(counts))/divide)

counts = [a,b,c,d]

ans = ''
alpha = "ABCD"
# print(counts)
while len(ans) != (a+b+c+d):
    covered = 0
    for i in range(len(counts)):
        if counts[i] >  0:
            new_counts = counts[:]
            new_counts[i] -= 1
            if covered + num_configs(new_counts) >= n:
                n-= covered
                ans += alpha[i]
                counts[i] -= 1
                break
            covered += num_configs(new_counts)
    # print(counts)
print(ans)



# print(num_configs(input()))
    