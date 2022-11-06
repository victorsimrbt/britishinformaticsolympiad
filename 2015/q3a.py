import math
import string

letters = string.ascii_uppercase

split = input().split()
counts,n = [int(val) for val in split[:4]],int(split[-1])
#print(counts)
path = []
def len_combos(counts):
    len_combos = math.factorial(sum(counts))
    for count in counts:
        len_combos = len_combos / math.factorial(count)
    return len_combos
def locate_string(counts,idx):
    global path
    if idx == 0 or counts == [0,0,0,0]:
        return True
    for i in range(len(counts)):
        if counts[i]:
            counts_copy = counts[:]
            counts_copy[i] -= 1
            section_length = len_combos(counts_copy)
            if idx > section_length:
                idx -= section_length
            else:
                path.append(i)
                if locate_string(counts_copy,idx):
                    return True
def list_2_string(path):
    final_string = ''
    for value in path:
        final_string += letters[value]
    return final_string
    

locate_string(counts,n)
#2 3 4 5 1234567print(path)
print(list_2_string(path))
    