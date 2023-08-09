import string
def lazy(curved):
    return curved[0],curved

def flipflop(curved):
    return curved[0],list(reversed(curved))

class Point:
    def __init__(self,char):
        self.char = char
        self.straight = None
        # LEFT TO RIGHT
        self.curved = None
        self.type = lazy
    def entry(self,point):
        if point in self.curved:
            if self.type == lazy:
                self.curved.remove(point)
                self.curved.insert(0,point)
            return self.straight
        if point == self.straight:
            exit_point = self.curved[0]
            if self.type == flipflop:
                self.curved.reverse()
            return exit_point
    def __str__(self):
        return self.char

A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X = [Point(char) for char in string.ascii_uppercase[:24]]
points = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X]

A.straight = D
A.curved = [E,F]

B.straight = C
B.curved = [G,H]

C.straight = B
C.curved = [I,J]

D.straight = A
D.curved = [K,L]

E.straight = A
E.curved = [M,N]

F.straight = A
F.curved = [N,O]

G.straight = B
G.curved = [O,P]

H.straight = B
H.curved = [P,Q]

I.straight = C
I.curved = [Q,R]

J.straight = C
J.curved = [R,S]

K.straight = D
K.curved = [S,T]

L.straight = D
L.curved = [T,M]

M.straight = U
M.curved = [L,E]

N.straight = U
N.curved = [E,F]

O.straight = V
O.curved = [F,G]

P.straight = V
P.curved = [G,H]

Q.straight = W
Q.curved = [H,I]

R.straight = W
R.curved = [I,J]

S.straight = X
S.curved = [J,K]

T.straight = X
T.curved = [K,L]

U.straight = V
U.curved = [M,N]

V.straight = U
V.curved = [O,P]

W.straight = X
W.curved = [Q,R]

X.straight = W
X.curved = [S,T]


def move(position):
    start,destination = list(position)
    start_point,destination_point = points[string.ascii_uppercase.index(start)],points[string.ascii_uppercase.index(destination)]
    return destination_point.entry(start_point)

flip_flops = list(input())
for point in flip_flops:
    points[string.ascii_uppercase.index(point)].type = flipflop

position = input()

for i in range(int(input())):
    new_point = move(position)
    position = position[-1]+new_point.char
print(position)
