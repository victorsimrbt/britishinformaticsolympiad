'''
(17, 29), (23, 23), (3, 43), (5, 41)
'''
import math
import time
# math.isprime()
isprime = [True] * 10000
isprime[0] = False
isprime[1] = False
def sieve():
    for f in range(2,10000):
        if isprime[f]:
            # print(f)
            for m in range(2,10000//f):
                # print("NOT PRIME",f*m)
                isprime[f*m] = False
                # time.sleep(1)
    # return primes

sieve()
primes = [i for i in range(10000) if isprime[i]]

def twoprime(num):
    ways = set()
    # ans = 0
    for i in range(len(primes)):
        if num - primes[i] in primes:
            # print(num-primes[i],primes[i])
            ways.add(tuple(sorted([num-primes[i],primes[i]])))
            # ways.add(primes[i])
            # ans += 1
    # print(ways)
    return len(ways)

ans = 0
for i in range(4,51):
    if i % 2 == 1:
        ways = twoprime(i)
        if ways == 0:
            ans += 1
            print(i)
# print(twoprime(int(input())))
# # for i in range(1000):
# #     if isprime[i]:
# #         print(i)
# # print(isprime)

# # def twoprime(num):
# #     ans = 0
# #     ways = set()
# #     for prime in primes:
# #         if num - prime in primes and not num in ways and not prime in ways:
# #             ways.add(num)
# #             ways.add(prime)
# #             ans += 1
# #     return ans

# # print(sieve(nums))