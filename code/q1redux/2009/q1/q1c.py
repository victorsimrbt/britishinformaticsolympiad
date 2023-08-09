'''
12
20
'''
digits = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT","NINE"]
word = "ONETWOTHREEFOURFIVE"

string = "FIVTWONHUREE"
print(len(set(string)))
print(len(string))
for digit in digits:
    chars = list(digit)
    for char in string:
        if char == chars[0]:
            chars.pop(0)
        if len(chars) == 0:
            print(digit)
            break

print()
string = "SEIFOTHURWVENX"

print(len(set(string)))
print(len(string))
for digit in digits:
    chars = list(digit)
    for char in string:
        if char == chars[0]:
            chars.pop(0)
        if len(chars) == 0:
            print(digit)
            break
        