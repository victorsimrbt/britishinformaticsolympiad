word1 = input()
word2 = input()

def get_counts(string):
    counts = {}
    for char in string:
        if not char in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

ans = get_counts(word1) == get_counts(word2)
if ans:
    print("Anagrams")
else:
    print("Not anagrams")
        