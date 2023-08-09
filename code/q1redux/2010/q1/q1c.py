'''
138
'''
import time
def get_counts(string):
    counts = {char:0 for char in string}
    for char in string:
        counts[char] += 1
    return counts

def no_dups(string):
    counts = get_counts(string)
    for val in counts.values():
        if val > 1:
            return False
    return True
        
def is_anagram(string1,string2):
    counts1 = get_counts(string1)
    counts2 = get_counts(string2)
    return counts1 == counts2
ans = 0
for i in range(100000,1000000):
    inpt = i
    if no_dups(str(inpt)):
        for mult in range(2,10):
            num1 = str(inpt)
            num2 = str(inpt*mult)
            if is_anagram(num1,num2):
                print(inpt)
                ans += 1
                break
print(ans)
    