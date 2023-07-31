import time
convert = {
    1:"I",
    5:"V",
    10:"X",
    50:"L",
    100:"C",
    500:"D",
    1000:"M",
    4 : "IV",
    9 : "IX",
    40 : "XL",
    400: "CD",
    900: "CM"
}

valid = sorted(convert.keys(),reverse=True)
print(valid)
def num_to_rom(num):
    rom = ""
    while num > 0:
        for key in valid:
            if num >= key:
                # print("KEY",key)
                num -= key
                rom += convert[key]
        # print(num,rom)
        # time.sleep(1)
    return rom

def lookandsay(string):
    ans = ''
    identical_len = 1
    identical_char = string[0]
    for i in range(1,len(string)):
        if string[i] == identical_char:
            identical_len += 1
        else:
            ans += num_to_rom(identical_len) + identical_char
            identical_char = string[i]
            identical_len = 1

    ans += num_to_rom(identical_len) + identical_char
    return ans
    
    
# print(num_to_rom(401))
for i in range(1,4000):
    rom = num_to_rom(i)
    print(lookandsay(rom))
    time.sleep(0.1)
    
'''
4
II
III
IV
IX
'''