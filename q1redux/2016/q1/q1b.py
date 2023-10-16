'''
3/5 + 1/5 = 4/5

4/5 = 1/3 + 3/2

LRRR
'''
import fractions


class :
    def __init__(self):
        self.numerator = None
        self.denominator = None
    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)
        pass

def promenade(string):
    if string == "":
        return fractions.Fraction(1/1)
    if string == "L":
        return fractions.Fraction(1/2)
    if string == "R":
        return fractions.Fraction(2/1)
    
    frac1 = fraction()
    # print(frac1)
    frac1.numerator = 0
    frac1.denominator = 1
    for i in reversed(range(len(string))):
        if string[i] == "R":
            # print(i,string[:i])
            frac1 = promenade(string[:i])
            break
    
    frac2 = fraction()
    frac2.numerator = 1
    frac2.denominator = 0
    for i in reversed(range(len(string))):
        if string[i] == "L":
            # print(i,string[:i])
            frac2 = promenade(string[:i])
            break
    
    # print(frac1,frac2)
    ans = fractions.Fraction(frac1.numerator+frac2.numerator,
                             frac1.denominator+frac2.denominator)
    return ans

for char1 in "LR":
    for char2 in "LR":
        for char3 in "LR":
            for char4 in "LR":
                # print(char1,char2,promenade(char1+char2))
                if promenade(char1+char2+char3+char4) == fractions.Fraction(4,5):
                    print(char1+char2+char3+char4)
        
        
