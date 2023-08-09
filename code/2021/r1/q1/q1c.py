import itertools
import string

letters = string.ascii_uppercase
letters_1 = "ACDEFGHIJKLMNOPQRSTUVWXYZ"

output = {
    True : "YES",
    False: "NO"
}
def alpha_after(string_1,string_2):
    idx_1 = [letters.index(char) for char in string_1]
    idx_2 = [letters.index(char) for char in string_2]
    
    return max(idx_1) < min(idx_2)

def is_pat(string):
    if len(string) ==  1:
        # print("ONE")
        return True
    for i in range(1,len(string)):
        left = string[:i]
        right = string[i:]
        # print(left,right,alpha_after(right,left))
        if (is_pat(''.join(reversed(left))) and 
            is_pat(''.join(reversed(right))) and 
            alpha_after(right,left)):
            return True
    return False

counter = 0
total_counter = 0
print(len(list(itertools.permutations(letters_1))))
for config in itertools.permutations(letters_1):
    config = "B" + ''.join(config)
    if is_pat(config):
        print("YAH",config)
        counter += 1
print(counter)
    