all_numbers = [i for i in range(1,10000)]

def check_prime(num):
    for number in all_numbers[:num]:
        if num % number == 0 and num != number and number != 1:
            return False
    return True

prime_numbers = [number for number in all_numbers[1:] if check_prime(number)]
import math
def search(num):
    pairs = [list(sorted([number,num-number])) for number in prime_numbers if number < num and num-number in prime_numbers]
    ways = [len(pairs)/2 if len(pairs) % 2 == 0 else len(pairs)//2+1]
    return ways[0]

count = 0
for i in range(4,51):
    if not(search(i)):
        count += 1
print(count)

