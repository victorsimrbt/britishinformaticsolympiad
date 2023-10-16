def construct_plan(plan):
    plan = list(plan)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:len(plan)+2]
    alphabet = list(alphabet)
    env = {alphabet[i] : [] for i in range(len(plan)+2)} 
    while plan:
        for char in alphabet:
            if not char in plan:
                env[char].append(plan[0])
                env[plan[0]].append(char)
                # print("WHAT",char,plan[0])
                # print(env[char],env[plan[0]])
                plan.pop(0)
                alphabet.remove(char)
                break
    # print(alphabet)
    env[alphabet[0]].append(alphabet[1])
    env[alphabet[1]].append(alphabet[0])
    for term in env:
        env[term] = sorted(env[term])
        print(''.join(env[term]))
    return env

def next_room(room):
    even_entrance[room] = not(even_entrance[room])
    if not(even_entrance[room]):
        exit_room = connections[room][0]
        even_exits[room][0] = not(even_exits[room][0])
        return exit_room
    else:
        exits = even_exits[room]
        for i in range(len(exits)):
            if not(exits[i]):
                if i == len(exits)-1:
                    exit_room = connections[room][i]
                    even_exits[room][i] = not(even_exits[room][i])
                else:
                    exit_room = connections[room][i+1]
                    even_exits[room][i+1] = not(even_exits[room][i+1])
                break
        return exit_room
    
plan,p,q = input().split()
p,q = int(p),int(q)
connections = construct_plan(plan)
even_entrance = {term:True for term in connections}
even_exits = {term:[True for i in range(len(connections[term]))] for term in connections}

# print(connections)
room = "A"
for i in range(p):
    room = next_room(room)
print(room,end="")

even_entrance = {term:True for term in connections}
even_exits = {term:[True for i in range(len(connections[term]))] for term in connections}

room = "A"
for i in range(q):
    room = next_room(room)
print(room)