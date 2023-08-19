'''
different starting position means shifting the array by n

clockwise and anticlockwise means that reversing the array is possible


 X O'
O O E
X   O
 X X
 
giveup
'''

def shift(seq):
    configs = []
    for x in range(len(seq)):
        # print(x)
        # print(seq[-x:],seq[:-x])
        configs.append(seq[-x:]+seq[:-x])
    return configs

def rotate(seq):
    # print(seq)
    return seq[0]+''.join(reversed(seq[1:]))


chars = ["O","X"]
ans = 0
checked = 0
layouts = set()
for char1 in range(2):
    for char2 in range(2):
        for char3 in range(2):
            for char4 in range(2):
                for char5 in range(2):
                    for char6 in range(2):
                        for char7 in range(2):
                            for char8 in range(2):
                                for char9 in range(2):
                                    for x in range(1,8):
                                        sequence = list(chars[char1] + chars[char2] + chars[char3] + chars[char4] + chars[char5] + chars[char6] + chars[char7] + chars[char8] + chars[char9])
                                        sequence[0] = "X"
                                        sequence[x] = "E"
                                        sequence = ''.join(sequence)
                                        if list(sequence).count("O") == 4:
                                            shifted = shift(sequence) + [sequence]
                                            # equivalent = shifted[:]
                                            equivalent = []
                                            for seq in shifted:
                                                equivalent.append(rotate(seq))
                                            # print(equivalent[0])
                                            equivalent = equivalent[:-1]
                                            seen = False
                                            for config in equivalent:
                                                if config in layouts:
                                                    seen = True
                                                layouts.add(config)
                                            if not(seen):
                                                ans += 1
                                                print(sequence)
                                        checked += 1
                                
                                

print(ans)