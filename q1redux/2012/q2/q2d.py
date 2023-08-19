import time
class Point:
    def __init__(self,char):
        self.char = char
        self.straight = "1"
        self.curved = "1"
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
        raise ValueError("The entrance {} is not connected to Point {}".format(entrance,self.char))
            
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

ans = 0
count = 0
all_pos = []
connections = ['ADEF', 'BCGH', 'CBIJ', "DAKL","EAMN","FANO","GBOP","HBPQ","ICQR","JCRS","KDST","LDTM","MULE","NUEF","OVFG","PVGH","QWHI","RWIJ","SXJK","TXKL","UVMN","VUOP","WXQR","XWST"]
for pt in connections:
	all_pos.append(pt[0] + pt[1])
	all_pos.append(pt[0] + pt[2])
	all_pos.append(pt[0] + pt[3])

for char1 in range(len(alphabet)):
    for char2 in range(char1+1,len(alphabet)):
        for char3 in range(len(alphabet)):
            for char4 in range(char3+1,len(alphabet)):
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
                fail = False
                from1,to1 = alphabet[char1],alphabet[char2]
                from2,to2 = alphabet[char3],alphabet[char4]
                if (to1 in points[from1].curved or to1 in points[from1].straight) and (to2 in points[from2].curved or to2 in points[from2].straight):
                    orig = from1,to1,from2,to2
                    print(orig)
                    # print(orig)
                    for i in range(72):
                        # print("GO",from1,to1,from2,to2)
                        if to1 == to2:
                            # ! going to the same point
                            # ! wrong
                            fail = True
                            # print("END")
                            break
                        
                        if set([from1,to1]) == set([from2,to2]):
                            # ! A E and E A
                            fail = True
                            # print("END")
                            break
                            
                        # if from1 == from2:
                        #     fail= True
                        #     break
                        # print("WHAT1",from1,to1)
                        from1,to1 = move(from1,to1)
                        # print("WHAT2",from2,to2)
                        from2,to2 = move(from2,to2)
                    if not(fail):
                        ans += 1
                        print(orig)
                    count += 1
                # time.sleep(1)
print(ans,count)
exit()
# flipflop = input()
for char in flipflop:
    points[char].is_lazy = False
from_pt,to_pt = input()
n = int(input())

for i in range(n):
    from_pt,to_pt = move(from_pt,to_pt)
print(from_pt+to_pt)