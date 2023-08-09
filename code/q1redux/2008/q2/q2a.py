rotor1 = {
    "A" : "A",
    "B" : "D",
    "C" : "B",
    "D" : "C",
}

rotor2 = {
    "A" : "A",
    "B" : "C",
    "C" : "B",
    "D" : "D",
}

reflector = {
    "A" : "D",
    "B" : "C",
    "C" : "B",
    "D" : "A"
}

translate = {
    "D" : "C",
    "A" : "D",
    "B" : "A",
    "C" : "B"
}

def backward(char,rotor):
    for key in rotor.keys():
        if rotor[key] == char:
            return key

def rotate(rotor):
    left = list(rotor.keys())
    right = list(rotor.values())
    
    left = [translate[char] for char in left]
    right = [translate[char] for char in right]
    # print(left,right)
    new_rotor = {left[i]:right[i] for i in range(len(left))}
    new_rotor = {key:new_rotor[key] for key in sorted(new_rotor.keys())}
    return new_rotor

def encode(char,rotor1,rotor2,reflector):
    # ? Works
    # ! forward pass
    encode_1 = rotor1[char]
    encode_2 = rotor2[encode_1]
    reverse = reflector[encode_2]
    
    # ! backwards pass
    backward_1 = backward(reverse,rotor2)
    backward_2 = backward(backward_1,rotor1)
    return backward_2

n = int(input())

# print(rotate(rotor1))

for i in range(n % 4):
    rotor1 = rotate(rotor1)


# # ! rotor2 is turned n//4 times
for i in range(n//4 % 4):
    rotor2 = rotate(rotor2)
    
# print(rotate(rotor2))
# for i in range(1,n+1):
#     print("rotor1 turned")
#     rotor1 = rotate(rotor1)
#     if i % 4 == 0 and i != 0:
#         print("rotor2 turned")
#         rotor2 = rotate(rotor2)
    
word = input()

ans = ''
idx = 0
while len(ans) != len(word):
    ans += encode(word[idx],rotor1,rotor2,reflector)
    idx += 1
    n += 1
    rotor1 = rotate(rotor1)
    if n % 4 == 0:
        rotor2 = rotate(rotor2)
print(ans)
# print(rotor1)
# print(encode("A",rotor1,rotor2,reflector))
