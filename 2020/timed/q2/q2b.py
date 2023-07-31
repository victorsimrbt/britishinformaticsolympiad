'''
1. A
2. AAAA
'''
# plan = input()
# p,q = int(p),int(q)

alphabet = list("ABCDEFGHIJKLMNOPQRSTUV")[:6]
alpha_complex = {letter:[] for letter in alphabet}
visits = {letter:True for letter in alphabet} # ! is even

def generate_complex(plan):
    plan = list(plan)
    rooms = list(alphabet[:len(plan)+2])
    chosen = []
    
    while plan:
        for room in rooms:
            if not room in chosen and not room in plan:
                chosen.append(room)
                alpha_complex[plan[0]].append(room)
                alpha_complex[room].append(plan[0])
                # print(plan[0],room)
                plan.pop(0)
                rooms.remove(room)
                break
    
    alpha_complex[rooms[0]].append(rooms[1])
    alpha_complex[rooms[1]].append(rooms[0])
# generate_complex("AAAA")
# exit()
for letter_1 in alphabet:
    for letter_2 in alphabet:
        for letter_3 in alphabet:
            for letter_4 in alphabet:
                alpha_complex = {letter:[] for letter in alphabet}
                plan = letter_1+letter_2+letter_3+letter_4
                generate_complex(plan)
                if len(alpha_complex["A"]) == 5:
                    print(alpha_complex)
                    print(plan)