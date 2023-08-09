'''
29
'''
ans = 0
for num1 in range(1,11):
    for num2 in range(num1,11):
        for num3 in range(num2,11):
            for num4 in range(num3,11):
                for num5 in range(num4,11):
                    sum15 = set()
                    cards = [num1,num2,num3,num4,num5]
                    if sum(cards) == 15:
                        ans += 1
                        print(cards)
print(ans)