plan,p,q=input().split()
p,q = int(p),int(q)
# ! is even

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

def get_exit(room):
    # print("CURRENTLY IN ROOM {}".format(room))
    # print(room,exit_visits[room],alpha_complex[room],visits[room])
    visits[room] = not(visits[room])
    if not(visits[room]): # ! is even
        exit_visits[room][0] = not(exit_visits[room][0]) # ! is even
        return alpha_complex[room][0]
    else:
        for i in range(len(alpha_complex[room])):
            if not(exit_visits[room][i]): 
                if i == len(alpha_complex[room]) - 1:
                    exit_visits[room][i] = not(exit_visits[room][i])
                    return alpha_complex[room][i]
                else:
                    exit_visits[room][i+1] = not(exit_visits[room][i+1])
                    return alpha_complex[room][i+1]
                

# alpha_complex["X"] = ["B","I","O"]
# visits["X"] = True
# exit_visits = {}
# exit_visits["X"] = [0,0,0]
# for i in range(5):
#     print(get_exit("X"))
# exit()
ans = ''
alphabet = list("ABCDEFGHIJKLMNOPQRSTUV")[:len(plan)+2]
alpha_complex = {letter:[] for letter in alphabet}
visits = {letter:True for letter in alphabet} 
generate_complex(plan)

exit_visits = {}
for key in alpha_complex:
    alpha_complex[key] = list(sorted(alpha_complex[key]))
    print(''.join(alpha_complex[key]))
    exit_visits[key] = [True for i in range(len(alpha_complex[key]))]

current = "A"
for x in range(p):
    
    current = get_exit(current)
    # print(current)
ans += current

# print("q")
# print("VISITS",visits)
alphabet = list("ABCDEFGHIJKLMNOPQRSTUV")[:len(plan)+2]
alpha_complex = {letter:[] for letter in alphabet}
visits = {letter:True for letter in alphabet} 
generate_complex(plan)
exit_visits = {}
for key in alpha_complex:
    alpha_complex[key] = list(sorted(alpha_complex[key]))
    # print(''.join(alpha_complex[key]))
    exit_visits[key] = [True for i in range(len(alpha_complex[key]))]
current = "A"
for x in range(q):
    current = get_exit(current)
    # print(current)
ans += current

print(ans)

'''
ABCDEF

1 A (odd)
2 B (odd)
3 A (even)
4 C (odd)
5 A (odd)
6 

A B A C 
'''
    
    