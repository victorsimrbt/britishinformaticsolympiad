import string
def generate_dial(n):
    alphabet = list(string.ascii_uppercase)
    dial = []
    start = -1

    for i in range(26):
        start = (n+start)%len(alphabet)
        new_letter = alphabet[start]
        alphabet.pop(start)
        start-=1
        dial.append(new_letter)
    return dial

def rotate(dial):
    first = dial.pop(0)
    dial.append(first)
    return dial

n,word = input().split()
n = int(n)
alphabet = list(string.ascii_uppercase)
dial = generate_dial(n)
print(''.join(dial[:6]))
ans = ''
for char in word:
    translate = {alphabet[i]:dial[i] for i in range(26)}
    ans+=translate[char]
    dial = rotate(dial)
    
print(ans)