import time

n = int(input())
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
distinct = set(fact(n,[]))
ans = 1
for term in distinct:
    ans *= term
print(ans)

# print(time.time()-start)
# print(primes)
# print(primes)
        