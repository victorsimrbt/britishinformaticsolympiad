turn_dict = {
    "A":"D",
    "B":"A",
    "C":"B",
    "D":"C"
    }


class Rotor:
    def __init__(self,config):
        self.config = config
    def forward(self,char):
        return self.config[char]
    def backward(self,char):
        return list(self.config.keys())[list(self.config.values()).index(char)]
    def turn(self):
        new_keys = [turn_dict[value] for value in list(self.config.keys())]
        new_values = [turn_dict[value] for value in list(self.config.values())]
        self.config = dict(sorted(zip(new_keys,new_values)))
        
rotor1_config = {
    "A":"A",
    "B":"D",
    "C":"B",
    "D":"C"
    }
rotor2_config = {
    "A":"A",
    "B":"C",
    "C":"B",
    "D":"D"
    }
reflector = {
    "A":"D",
    "B":"C",
    "C":"B",
    "D":"A"
    }

rotor1 = Rotor(rotor1_config)
rotor2 = Rotor(rotor2_config)


def forward_pass(char):
    rotor1_pass1 = rotor1.forward(char)
    rotor2_pass1 = rotor2.forward(rotor1_pass1)
    reflector_pass = reflector[rotor2_pass1]
    rotor2_pass2 = rotor2.backward(reflector_pass)
    rotor1_pass2 = rotor1.backward(rotor2_pass2)
    result = rotor1_pass2
    return result

base_turns = int(input())
letter = input()
counter = 0

counter = base_turns
rotor1_rotations = [base_turns % (1*4) if base_turns // (1*4) else 0]
rotor2_rotations = [base_turns // 4 % 4 if base_turns // 4 % 4 else 0]

for _ in range(rotor1_rotations[0]):
    rotor1.turn()
    
for _ in range(rotor2_rotations[0]):
    rotor2.turn()

encrypted = []
for i in range(len(letter)):
    encrypted.append(forward_pass(letter[i]))
    rotor1.turn()
    if (counter+1) % 4 == 0:
        rotor2.turn()
    counter += 1

print(''.join(encrypted))



