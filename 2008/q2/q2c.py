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
    
    last_config = config[0]
    for i in range(100):
        rotor1.turn()
        if rotor1.config != last_config:
            fail = True
            break
        last_config = rotor1.config
    
    last_config = config[1]
    for i in range(4):
        rotor2.turn()
        if rotor2.config != last_config:
            fail = True
            break
        last_config = rotor2.config
        
    if not(fail):
        print(config[0].values(),config[1].values())