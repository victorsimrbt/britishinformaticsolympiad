'''
1. 4
2. 192
'''
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
    
from itertools import permutations
alphabet = 'ABCD'
configs = list(permutations(alphabet))

rotor = {
    "A" : "A",
    "B" : "D",
    "C" : "B",
    "D" : "C",
}

# def encode(char,rotor1,reflector):
#     encode_1 = rotor1[char]
#     reverse = reflector[encode_1]
    
#     return backward(reverse,rotor1)
ans = 0
for config1 in configs:
    for config2 in configs:
        rotor1 = {list(rotor.keys())[i]:config1[i] for i in range(len(rotor))}
        rotor2 = {list(rotor.keys())[i]:config2[i] for i in range(len(rotor))}
        # print(rotor["A"])
        fail = False
        for i in range(100):
            if (encode("A",rotor1,rotor2,reflector) == "B" and
                encode("B",rotor1,rotor2,reflector) == "A" and 
                encode("C",rotor1,rotor2,reflector) == "D" and 
                encode("D",rotor1,rotor2,reflector) == "C"):
                # print("pass")
                pass
            else:
                fail = True
                break
            rotor1 = rotate(rotor1)
            if i % 4 == 0:
                rotor2 = rotate(rotor2)
        if not(fail):
            print(''.join(config1),''.join(config2))
            ans += 1
print(ans)
