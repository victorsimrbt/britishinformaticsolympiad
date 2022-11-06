import string
letters = string.ascii_uppercase

def fibonacci_letters(letter1,letter2,n):
    terms = [letters[letter1-1],letters[letter2-1]]
    last_two = [letter1,letter2]
    
    for i in range(10000):
        new_term = [sum(last_two)-26 if sum(last_two) > 26 else sum(last_two)][0]
        #print(new_term)
        last_two.append(new_term)
        last_two = last_two[-2:]
        terms.append(letters[new_term-1])
        
        if len(terms) > 10 and terms[-5:] == terms[:5]:
            repeating_terms = terms[:][:-5]
            break
    #print(''.join(repeating_terms))
    #print(repeating_terms)
    #Zprint(n%len(repeating_terms))
    return repeating_terms[n % len(repeating_terms)-1]

letter_1,letter_2,n = input().split()
n = int(n)


terms = fibonacci_letters(letters.index(letter_1)+1,letters.index(letter_2)+1,n)
print(''.join(terms))