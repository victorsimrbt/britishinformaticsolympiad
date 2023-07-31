'''

'''
import time
# print("HIGH")
alphabet = list("ABCDEFGHIJKLMNOPQRSTUV")[:8]
alpha_complex = {letter:[] for letter in alphabet}
visits = {letter:True for letter in alphabet} # ! is even

optimal = {'A': ['E'], 'B': ['F'], 'C': ['G'], 'D': ['H'], 'E': ['A'], 'F': ['B'], 'G': ['C'], 'H': ['D']}
def generate_complex(plan):
    cons = ["AE","BF","CG","DH"]
    plan = list(plan)
    rooms = list(alphabet[:len(plan)+2])
    chosen = []
    
    counter = 0
    while plan:
        for room in rooms:
            if not room in chosen and not room in plan:
                counter += 1
                
                if room+plan[0] in cons:
                    cons.remove(room+plan[0])
                elif plan[0]+room in cons:
                    cons.remove(plan[0]+room)
                
                # if counter == 4:
                #     return
                alpha_complex[plan[0]].append(room)
                alpha_complex[room].append(plan[0])
                # print(plan[0],room)
                plan.pop(0)
                rooms.remove(room)
                if counter == 5:
                    # print(alpha_complex)
                    # print(alpha_complex)
                    if len(cons) == 0:
                        return True
                    
                break
    
    alpha_complex[rooms[0]].append(rooms[1])
    alpha_complex[rooms[1]].append(rooms[0])

def generate_complex2(plan):
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
generate_complex2(input())
print(alpha_complex)
# exit()
ans = 0
for letter_1 in alphabet:
    for letter_2 in alphabet:
        for letter_3 in alphabet:
            for letter_4 in alphabet:
                for letter_5 in alphabet:
                    for letter_6 in alphabet:
                        alpha_complex = {letter:[] for letter in alphabet}
                        plan = letter_1+letter_2+letter_3+letter_4+letter_5+letter_6
                        # print(plan)
                        if generate_complex(plan):
                            print(plan)
                            ans += 1
                        # time.sleep(0.5)
                        # if len(alpha_complex["A"]) == 5:
                        #     print(alpha_complex)
                        #     print(plan)
print(ans)

'''
54
'''