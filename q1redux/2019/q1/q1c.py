'''
9030
'''
palindromes = [0]
ans = 0
for i in range(1,100000):
    if str(i) == ''.join(reversed(str(i))):
        palindromes.append(i)
        # print(i)
    
    can_sum = False
    for palindrome in palindromes:
        if i - palindrome in palindromes:
            can_sum = True
            break
    if not(can_sum):
        # print("WOAH",i)
        ans += 1
    if i % 100 == 0:
        print(i)
print("ANS",ans)