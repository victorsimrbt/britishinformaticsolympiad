from itertools import combinations_with_replacement, permutations,combinations
# ! SOMEHOW I DON'T GET 32
from cv2 import bilateralFilter 
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
        
all_configs = [dict(zip(list(turn_dict.keys()),permutation)) for permutation in permutations("ABCD")]
rotor1_config = {
    "A":"A",
    "B":"D",
    "C":"B",
    "D":"C"
    }
rotor = Rotor(rotor1_config)
rotor.turn()
print(rotor.config)
rotor.turn()
print(rotor.config)

print("ONE ROTOR")
working_configs = []
for config in all_configs:
    fail = False
    rotor_test= Rotor(config)
    last_config = config
    for i in range(4):
        rotor_test.turn()
        if rotor_test.config != last_config:
            fail = True
            break
        last_config = rotor_test.config
    if not(fail):
        working_configs.append(config)
        print(config.values())

        
all_configs = list(permutations(all_configs,2))
print(len(all_configs))

print("TWO ROTORS")
for config in all_configs:
    fail = False
    rotor1 =  Rotor(config[0])
    rotor2 =  Rotor(config[1])
    
    encrypted = []
    combine_dict = {}
    for key in list(rotor1.config.keys()):
        combine_dict[key] = rotor2.config[rotor1.config[key]]
    prev_dict = combine_dict
    for i in range(16):
        rotor1.turn()
        if (i+1) % 4 == 0:
            rotor2.turn()
            
        combine_dict = {}
        for key in list(rotor1.config.keys()):
            combine_dict[key] = rotor2.config[rotor1.config[key]]
        if combine_dict != prev_dict:
            fail = True
            break
        prev_dict = combine_dict
    if not(fail):
        working_configs.append(config)
        print(rotor1.config)
        print(rotor2.config)
        print()