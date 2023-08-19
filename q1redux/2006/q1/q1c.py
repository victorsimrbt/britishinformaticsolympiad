'''
21

'''
chars = "ABC"

def get_counts(string):
    counts = {char:0 for char in chars}
    # print(counts)
    for char in string:
        # if not char in counts:
        #     counts[char] = 1
        # else:
        counts[char] += 1
    return counts

option = set()
for char1 in chars:
    for char2 in chars:
        for char3 in chars:
            for char4 in chars:
                for char5 in chars:
                    word = char1 + char2+ char3+char4+char5
                    counts = tuple(get_counts(word).values())
                    option.add(counts)
print(option)
print(len(option))
                    
                    