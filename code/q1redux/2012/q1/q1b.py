'''
10
20
40
50
80
100
160
200
250
320
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

def fact(num,factors):
    # print(num,factors)
    if num == 1:
        return factors
    ans = []
    for prime in primes:
        if num % prime == 0:
            ans += fact(num//prime,factors+[prime])
            break
    return ans
            

sieve()
success = 0
for n in range(1,1000000):
    distinct = set(fact(n,[]))
    ans = 1
    for term in distinct:
        ans *= term
    if ans == 10:
        print(n)
        success += 1
    if success == 10:
        break
# print(primes)
# print(primes)
        