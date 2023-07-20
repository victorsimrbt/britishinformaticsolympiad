import string
alphabet = string.ascii_uppercase
text = input()
new_txt = list()
for i in range(len(text)-1,0,-1):
    char_idx = alphabet.index(text[i])+1
    prev_idx = alphabet.index(text[i-1])+1
    
    if prev_idx > char_idx:
        original = 26-prev_idx+char_idx
    else:
        original = char_idx-prev_idx
    new_txt.insert(0,alphabet[original-1])
        
    
print(''.join([text[0]]+new_txt))