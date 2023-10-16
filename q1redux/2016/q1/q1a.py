import math
import fractions
# isprime = [True for i in range(101)]
# def sieve():
#     primes = []
#     for f in range(2,100):
#         if isprime[f]:
#             primes.append(f)
#             for mult in range(2,100//f+1):
#                 # print(f*mult,"is false")
#                 isprime[f*mult] = False
#     return primes

# primes = sieve()
# def factorise(num):
#     ans = []
#     if num in primes:
#         return [num]
#     for prime in primes:
#         factorise(num/prime)
# print(sieve())
# print(isprime)

class fraction:
    def __init__(self):
        self.numerator = None
        self.denominator = None
    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)
        pass
        
a = fraction()
# a.numerator = 2
# exit()

def promenade(string):
    if string == "":
        return fractions.Fraction(1/1)
    if string == "L":
        return fractions.Fraction(1/2)
    if string == "R":
        return fractions.Fraction(2/1)
    
    frac1 = fraction()
    # print(frac1)
    frac1.numerator = 0
    frac1.denominator = 1
    for i in reversed(range(len(string))):
        if string[i] == "R":
            # print(i,string[:i])
            frac1 = promenade(string[:i])
            break
    
    frac2 = fraction()
    frac2.numerator = 1
    frac2.denominator = 0
    for i in reversed(range(len(string))):
        if string[i] == "L":
            # print(i,string[:i])
            frac2 = promenade(string[:i])
            break
    
    # print(frac1,frac2)
    ans = fractions.Fraction(frac1.numerator+frac2.numerator,
                             frac1.denominator+frac2.denominator)
    return ans
    
    
            
    # print(frac1,frac2)
    
fraction = promenade(input())
print("{} / {}".format(fraction.numerator,fraction.denominator))

# def reduce(num,denom):
    
