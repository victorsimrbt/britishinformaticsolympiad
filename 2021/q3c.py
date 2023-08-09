alphabet = "ABCDEFGH"
def add(boxes):
    for letter in alphabet:
        if not(letter in boxes):
            return boxes + letter
    return boxes

def swap(boxes):
    if len(boxes) >= 2:
        boxes = list(boxes)
        temp = boxes[0]
        boxes[0] = boxes[1]
        boxes[1] = temp
        return ''.join(boxes)
    return boxes
    
def rotate(boxes):
    if len(boxes) > 1:
        return boxes[1:]+boxes[0]
    return boxes

def generate_neighbors(boxes):
    neighbors = []
    neighbors.append(add(boxes))
    neighbors.append(swap(boxes))
    neighbors.append(rotate(boxes))
    return neighbors

target = input()
dist = {}
queue = []
head = 0
queue.append('')
dist[''] = 0
while head < len(queue):
    # print(queue[head])
    last = queue[head]
    neighbors =  generate_neighbors(last)
    head += 1
    for neighbor in neighbors:
        if not(neighbor in dist):
            dist[neighbor] = dist[last] + 1
            queue.append(neighbor)
        if neighbor == target:
            print(dist[neighbor])
    