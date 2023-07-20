import string

alphabet = string.ascii_uppercase[:-1]

target = ""
input_string = input()
state = [0]*25
for char in input_string:
    if char.isupper():
        state[alphabet.index(char.upper())] += 2
    else:
        state[alphabet.index(char.upper())] += 1
visited = []

def state_str(state):
    string = ''
    for i in range(len(state)):
        if state[i] == 2:
            string += alphabet[i].upper()
        elif state[i] == 1:
            string += alphabet[i].lower()
    return string

def press_button(char,state):
    state = state[:]
    adjacent = update(char)
    for letter in adjacent:
        state[letter] = (state[letter]+1)%3
    return state

def print_lighting(state):
    print_string = ''
    for i in range(len(state)):
        if state[i] == 1:
            print_string += alphabet[i].lower()
        elif state[i] == 2:
            print_string += alphabet[i]
    return print_string
    

def update(char):
    idx = alphabet.index(char)
    adjacent = [idx]
    if idx > 4:
        adjacent.append(idx-5)
    if idx % 5 != 0:
        adjacent.append(idx-1)
    if idx % 5 != 4:
        adjacent.append(idx+1)
    if idx < 20:
        adjacent.append(idx+5)
    return adjacent

queue = []
head = 0
queue.append([state,''])
while head < len(queue):
    last = queue[head][0]
    steps = queue[head][1]
    head += 1
    for char in alphabet:
        new_state = press_button(char,last)
        if not(new_state in visited):
            if print_lighting(new_state) == target:
                print(print_lighting(new_state),steps+char)
                print("FOUND")
                # raise KeyboardInterrupt
            queue.append([new_state,steps+char])
            visited.append(new_state)
print("IMPOSSIBLE")