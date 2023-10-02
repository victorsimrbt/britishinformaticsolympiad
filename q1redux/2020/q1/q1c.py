'''
3919
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
unique = set()
for i in range(1,4000):
    # print(num2rom(i))
    result = lookandsay(num2rom(i))
    unique.add(result)
print(len(unique))