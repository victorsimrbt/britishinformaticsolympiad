'''
VU
UM
ML
LD
DA
AE
EM
MU
UV
VP
'''
class Point:
    def __init__(self,char):
        self.char = char
        self.straight = None
        self.curved = None
        self.is_lazy = True
    def get_exit(self,entrance):
        if entrance in self.straight:
            # ! coming from straight, exit via curved
            exit_char = self.curved[0]
            if self.is_lazy:
                pass
            else:
                # ! it is flip flop
                # reverse the list
                self.curved = ''.join(list(reversed(self.curved)))
            return exit_char
        if entrance in self.curved:
            exit_char = self.straight
            if self.is_lazy:
                if self.curved[0] == entrance:
                    pass
                else:
                    self.curved = ''.join(list(reversed(self.curved)))
            return exit_char
        assert ValueError("THE ENTRANCE IS NOT CONNECTED")
            
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWX" 
 
points = {char:Point(char) for char in alphabet}

points["A"].straight = "D"
points["A"].curved = "EF"

points["B"].straight = "C"
points["B"].curved = "GH"

points["C"].straight = "B"
points["C"].curved = "IJ"

points["D"].straight = "A"
points["D"].curved = "KL"

points["E"].straight = "A"
points["E"].curved = "MN"

points["F"].straight = "A"
points["F"].curved = "NO"

points["G"].straight = "B"
points["G"].curved = "OP"

points["H"].straight = "B"
points["H"].curved = "PQ"

points["I"].straight = "C"
points["I"].curved = "QR"

points["J"].straight = "C"
points["J"].curved = "RS"

points["K"].straight = "D"
points["K"].curved = "ST"

points["L"].straight = "D"
points["L"].curved = "TM"

points["M"].straight = "U"
points["M"].curved = "LE"

points["N"].straight = "U"
points["N"].curved = "EF"

points["O"].straight = "V"
points["O"].curved = "FG"

points["P"].straight = "V"
points["P"].curved = "GH"

points["Q"].straight = "W"
points["Q"].curved = "HI"

points["R"].straight = "W"
points["R"].curved = "IJ"

points["S"].straight = "X"
points["S"].curved = "JK"

points["T"].straight = "X"
points["T"].curved = "KL"

points["U"].straight = "V"
points["U"].curved = "MN"

points["V"].straight = "U"
points["V"].curved = "OP"

points["W"].straight = "X"
points["W"].curved = "QR"

points["X"].straight = "W"
points["X"].curved = "ST"

def move(from_pt,to_pt):
    exit_char = points[to_pt].get_exit(from_pt)
    return to_pt,exit_char

flipflop = input()
for char in flipflop:
    points[char].is_lazy = False
from_pt,to_pt = input()
n = int(input())

for i in range(n):
    from_pt,to_pt = move(from_pt,to_pt)
    print(from_pt+to_pt)
    # if to_pt == "P":
    #     break
# print(from_pt+to_pt)