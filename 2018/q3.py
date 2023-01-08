def generate_neighbours(n):
    neighbours = set()
    digits = [int(char) for char in str(n)]
    for i in range(len(digits)-1):
        smaller = min(digits[i],digits[i+1])
        bigger = max(digits[i],digits[i+1])
        
        adjacent_digits = [digits[x] for x in [i-1,i+2] if x >= 0 and x < len(digits)]
        for digit in adjacent_digits:
            if smaller < digit < bigger:
                digits_copy = digits[:]
                temp = digits_copy[i]
                digits_copy[i] = digits[i+1]
                digits_copy[i+1] = temp
                digits_copy =[str(char) for char in digits_copy]
                neighbours.add(int(''.join(digits_copy)))
    return neighbours

input()
queue = []
dist = {}
root = int(input())
dist[root] = 0
queue.append(root)
head = 0

while head < len(queue):
    last = queue[head]
    for neighbour in generate_neighbours(last):
        if not(neighbour in dist):
            queue.append(neighbour)
            dist[neighbour] = dist[last] + 1
    head += 1

print(max(dist.values()))
                