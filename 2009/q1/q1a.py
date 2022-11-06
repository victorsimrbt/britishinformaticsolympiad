digits = ['ONE', 'TWO', "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT" , "NINE"]

def check_string(string):
    checks = [list(digit) for digit in digits]
    for char in string:
        for check in checks:
            if check and char == check[0]:
                check.pop(0)
    present = [i+1 for i in range(len(checks)) if not(checks[i])]
    final_answer = [present[0] if present else "NO"][0]
    return final_answer
    
string = input()
print(check_string(string))
    