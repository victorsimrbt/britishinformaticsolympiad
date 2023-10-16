'''
4
II
III
IV
IX
'''
translate = {
        "I" : 1,
        "IV" : 4,
        "V" : 5,
        "IX" : 9,
        "X" : 10,
        "XL" : 40,
        "L" : 50,
        "XC" : 90,
        "C" : 100,
        "CD" : 400,
        "D" : 500,
        "CM" : 900,
        "M" : 1000
    }
size = list(translate.keys())
def num2rom(num):
    translate = {
        "I" : 1,
        "IV" : 4,
        "V" : 5,
        "IX" : 9,
        "X" : 10,
        "XL" : 40,
        "L" : 50,
        "XC" : 90,
        "C" : 100,
        "CD" : 400,
        "D" : 500,
        "CM" : 900,
        "M" : 1000
    }
    elements = list(reversed(translate))
    ans = ''
    while True:
        for element in elements:
            if translate[element] <= num:
                num -= translate[element]
                ans += element
                break
        if num == 0:
            return ans
        
def lookandsay(string):
    ans = ''
    prev = string[0]
    length = 0
    for i in range(len(string)):
        if string[i] == prev:
            length += 1
        else:
            # print(length,string[i-1])
            ans += num2rom(length)+string[i-1]
            prev = string[i]
            length = 1
        if i == len(string)-1:
            # print(length,string[i-1])
            ans += num2rom(length)+string[i]
            prev = string[i]
            length = 1
    return ans

ans = 0
for i in range(1,4000):
    # print(num2rom(i))
    result = lookandsay(num2rom(i))
    # print("NUMBER",i,num2rom(i))
    invalid = False
    prev = result[0]
    length = 0
    for i in range(len(result)):
        if result[i] == prev:
            length += 1
        else:
            if length > 3:
                invalid = True
            length = 1
            prev = result[i]
    
    # print(length)
    if length > 3:
        invalid = True
    
    indices = []
    i = 0
    while i < len(result):
        # print(result[i:i+2])
        if result[i:i+2] in translate:
            indices.append(size.index(result[i:i+2]))
            i += 2
        else:
            indices.append(size.index(result[i]))
            i += 1
    
    # print(indices)
    if not(indices == list(sorted(indices,reverse = True))):
        invalid = True
        
    if not(invalid):
        # print(i,num2rom(i))
        # print("VALID",result)
        # print()
        ans += 1
    print(result)
    print()
print(ans)