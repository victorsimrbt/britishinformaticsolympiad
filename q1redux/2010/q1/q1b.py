'''
28415970
17049582
14207985
'''
num = 85247910

def get_counts(string):
    counts = {char:0 for char in string}
    for char in string:
        counts[char] += 1
    return counts
        
def is_anagram(string1,string2):
    counts1 = get_counts(string1)
    counts2 = get_counts(string2)
    return counts1 == counts2
    
for i in range(2,10):
    if num % i == 0:
        generator = num//i
        if is_anagram(str(num),str(generator)):
            print(generator)