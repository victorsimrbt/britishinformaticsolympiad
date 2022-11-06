from itertools import permutations
no_dups = [i for i in range(100000,1000000) if sorted(list(str(i))) == sorted(set(list(str(i))))]
def anagram_numbers(number):
    number_list = [str(value) for value in str(number)]
    multiples = []
    for value in list(permutations(number_list)):
        scrambled = int(''.join(value))
        if scrambled > number and scrambled % number == 0:
            multiples.append(str(int(scrambled/number)))
    return [True if multiples else False][0]


print(len(no_dups))

anagram_nums = [instance for instance in no_dups if anagram_numbers(instance)]

print(len(anagram_nums))