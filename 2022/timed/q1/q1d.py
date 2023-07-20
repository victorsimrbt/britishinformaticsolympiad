import string
alphabet = string.ascii_uppercase

def encrypt(text):
    text = list(text)
    prev_idx = alphabet.index(text[0])
    for i in range(1,len(text)):
        idx = alphabet.index(text[i])+1
        prev_idx = alphabet.index(text[i-1])+1
        
        new_idx = (idx+prev_idx) % 26
        text[i] = alphabet[new_idx-1]
    return text

ans = 0
for char_1 in range(1,27):
    for char_2 in range(1,27):
        for char_3 in range(1,27):
            
            txt = '{}{}{}'.format(alphabet[char_1-1],
                                  alphabet[char_2-1],
                                  alphabet[char_3-1])
            original = txt
            counter = 0
            while True:
                txt = ''.join(encrypt(txt))
                counter += 1
                if txt == original:
                    break
            if 999999999999 % counter == 0:
                ans += 1
                # print(counter)
                # print(original)
                
# print(ans)

'''
ans = 24
'''
print(26*26*26,ans)
exit()

txt = "BBB"
for i in range(999):
    txt = ''.join(encrypt(txt))
    print("{}: {}".format(i+1,txt))
    
'''
(char_1 + char_2*999999) % 26 = char_2
(char_2 + char_3*999999) % 26 = char_3

char_2*999998 + char_1 is a multiple of 26
char_3*999998 + char_2 is a multiple of 26
'''
