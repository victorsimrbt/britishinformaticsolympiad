from itertools import permutations
'''
vobi
'''
translate = {
    "pa" : 1,
    "re" : 2,
    "ci" : 3,
    "vo" : 4,
    "mu" : 5,
    "xa" : 6,
    "ze" : 7,
    "bi" : 8,
    "so" : 9,
    "no" : 0,
}
alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphasum(string):
    ans = 0
    for char in string:
        print(alphabet.index(char) + 1)
        ans += alphabet.index(char) + 1
    return ans

def convert(string):
    ans = ''
    for i in range(0,len(string)-1,2):
        # print(string[:i+2])
        ans += str(translate[string[i:i+2]])
    return int(ans)
    
options = list(translate.keys())

print(alphasum("vobi"),convert("vobi"))
# for char1 in options:
#     for char2 in options:
#         string = char1+char2
#         if alphasum(string) == convert(string):
#             print(string)

