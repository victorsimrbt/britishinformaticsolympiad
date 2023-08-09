'''
30
'''
import time

# n = int(input())
# start = time.time()
isprime = [True] * 1000000
isprime[1] = False
primes = []
def sieve():
    for f in range(2,1000000):
        if isprime[f]:
            primes.append(f)
            for m in range(2,1000000//f+1):
                # print(f,f*m)
                # print(f*m)
                try:
                    isprime[f*m] = False
                except:
                    pass

memo = {}
def fact(num):
    # print(num)
    if num == 1:
        return [1]
    if num in memo:
        # print("MEMOD")
        return memo[num]
    else:
        ans = []
        for prime in primes:
            if num % prime == 0:
                # print("WHOAH",num//prime)
                ans.append(prime)
                ans += fact(num//prime)
                break
        memo[num] = ans
    return ans
            

sieve()
# print(fact(int(input())))
freq = {}
success = 0
for n in range(1,1000000):
    distinct = set(fact(n))
    ans = 1
    for term in distinct:
        ans *= term
    if ans in freq:
        freq[ans] += 1
    else:
        freq[ans] = 1
    if n % 10000 == 0:
        print(n)
        maximum = max(freq.values())
        print([key for key in freq if freq[key] == maximum])

maximum = max(freq.values())
print([key for key in freq if freq[key] == maximum])

# print(primes)
# print(primes)
        