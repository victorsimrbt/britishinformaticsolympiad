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

txt = "OLYMPIAD"
for i in range(1000):
    txt = ''.join(encrypt(txt))
    print("{}: {}".format(i+1,txt))
    if txt == "OLYMPIAD":
        print(i+1,"YEAH")
        break
    
'''
104 times
'''
