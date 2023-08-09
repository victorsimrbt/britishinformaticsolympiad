digits = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT","NINE"]


def is_digit(string):
    for digit in digits:
        chars = list(digit)
        for char in string:
            if char == chars[0]:
                chars.pop(0)
            if len(chars) == 0:
                return digit
    else:
        return False
        

ans = is_digit(input())
if ans:
    print(digits.index(ans)+1)
else:
    print("NO")