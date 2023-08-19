string = input()
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
ans = ''
for i in range(0,len(string)-1,2):
    # print(string[:i+2])
    ans += str(translate[string[i:i+2]])
print(ans)