from itertools import permutations
def anagram_numbers(number):
    number_list = [str(value) for value in str(number)]
    multiples = []
    for value in list(permutations(number_list)):
        scrambled = int(''.join(value))
        if scrambled > number and scrambled % number == 0:
            multiples.append(str(int(scrambled/number)))
    return [' '.join(sorted(set(multiples))) if multiples else "NO"][0]

number = int(input())
print(anagram_numbers(number))
    