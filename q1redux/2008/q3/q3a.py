import time
def op1(shirts):
    return shirts[1:4]+shirts[0]+shirts[4:]

def op2(shirts):
    return shirts[:3]+shirts[-1]+shirts[3:-1]

def op3(shirts):
    return shirts[3]+shirts[:3]+shirts[4:]

def op4(shirts):
    return shirts[:3]+shirts[4:]+shirts[3]

# print(op1("1234567"))
# print(op2("1234567"))
# print(op3("1234567"))
# print(op4("1234567"))

dist = {}
head = 0
root = input()
dist[root] = 0
queue = [root]
# maximum = 0
while head < len(queue):
    state = queue[head]
    neighbors = [op1(state),op2(state),op3(state),op4(state)]
    for neighbor in neighbors:
        if not neighbor in dist:
            dist[neighbor] = dist[state] + 1
            queue.append(neighbor)
        if neighbor == "1234567":
            print(dist[state]+1)
            exit()
    # print(queue)
    # time.sleep(1)
    head += 1
