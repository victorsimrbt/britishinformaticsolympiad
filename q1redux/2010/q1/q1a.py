def get_counts(string):
    counts = {char:0 for char in string}
    for char in string:
        counts[char] += 1
    return counts
        
def is_anagram(string1,string2):
    counts1 = get_counts(string1)
    counts2 = get_counts(string2)
    return counts1 == counts2
    
inpt = int(input())
ans = ''
for mult in range(2,10):
    num1 = str(inpt)
    num2 = str(inpt*mult)
    if is_anagram(num1,num2):
        ans += str(mult) + ' '

if ans == '':
    print("NO")
else:
    print(ans)
    