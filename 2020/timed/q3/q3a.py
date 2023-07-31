'''
p: first p letters of alphabet can be used
q: number of adjacent letters allowed
r: length of plan

observations:
equal number starting under a given letter
feels recursive
probably need to calculate the number of cases that break the rule under each bin

total number of rule breakers is the sum of rule breakers among each starting letter and so on

hits base case when the illegal number of adjacents are hit

find position and the number of illegals before it

no more than 3 adjacent

general formula:

number of illegal sequences:



number of possible characters * n**(total_length - illegal) * (total_length - illegal + 1)
*XXX*

AAAB

BBB

_ _ _ _ _
XXX..
.XXX.
..XXX

n

n^2

n^3 -  1

n^4 - 2*n^2

n^5 - 3*n^3

n^6 -

n ways to form XXX and n^4 ways to form XXX... and 4 ways to redistribute
XXX...
.XXX..
..XXX.
...XXX


n ways to form X.. and n^(length-adjacent limit) wys to form X..??? and then (length-adj limit to redistribute)

n ways to form 1 char

n^2 ways to form 2 char

n^3 - n ways to form 3 chars

n^4 - n*n*2 + duplicates(n) to form 4 chars

n^4 - n -  2(n*(n-1))
XXX.

AAAA
AAAB

BBBA
BBBB

.XXX

BAAA
AAAA

BBBB
ABBB

n^5 - n - 2(n * (n-1)) - 3(n * (n-1) * (n-1))

XXXXX
XXXX.
XXX..
..XXX
.XXX.
.XXXX
XXXX.

n^6 - n - 2(n * (n-1)) - 3(n * (n-1) * (n-1)) - 4(n*(n-1)*(n-1)*(n-1))

XXXXXX

XXXXX.
.XXXXX

XXXX..
.XXXX.
XXXX..

XXX...
.XXX..
..XXX.
...XXX

different window size but the characters on the edges cannot be the same







number of possibilities can be formulaically generated

method:
formulaically generate possibilities per layer and total possibilities

go through each layer and determine which bin it is in
use prev letters to determine list of options
XXX... 
.XXX..
..XXX.
...XXX

add an a and a b behind and ahead of each of the previous ones
and then use set
'''

def num_configs(p,q,r):
    # ! p is the number of letters
    # ! q is the adjacent allowed
    # ! r is the length
    '''
    number of possible characters * n**(total_length - illegal) * (total_length - illegal + 1)
    '''
    ans = p**r
    minus_term = p
    coefficient = 1
    for x in range(r-2):
        ans -= coefficient * minus_term
        print(minus_term)
        minus_term *= (p-1)
        coefficient += 1
    return ans
    # print(r-q)
    # print(r-q+1)
    # return p * p **(r-q-1) * (r-q+1)
    
def add_layer(configs):
    new_configs = []
    for config in configs:
        new_configs.append(config+"A")
        new_configs.append(config+"B")
    return new_configs

'''
[?*n]*
'''

ans = 0
configs = ["A","B","C"]
for x in range(10):
    for config in configs:
        prev = config[0]
        consecutive = 0
        for letter in config:x
            if prev == letter:
                consecutive += 1
            else:
                consecutive = 1
                prev = letter
            if consecutive >= 3:
                ans += 1
                # print("cons",config)
                break
        if consecutive == 3:
            print("cons",config)
        else:
            print(config)
        
    configs = add_layer(configs)
    print(ans)

# print(num_configs(2,3,6))
# letters = ["A","B"]
# ans = 0
# total = 0
# for letter_1 in letters:
#     for letter_2 in letters:
#         for letter_3 in letters:
#             for letter_4 in letters:
#                 for letter_5 in letters:
#                     for letter_6 in letters:
#                         word = letter_1 + letter_2 + letter_3+letter_4 + letter_5+letter_6
#                         consecutive = 0
#                         prev = word[0]
                        
#                         for letter in word:
#                             if prev == letter:
#                                 consecutive += 1
#                             else:
#                                 consecutive = 1
#                                 prev = letter
#                             if consecutive >= 3:
#                                 print("cons",word)
#                                 ans += 1
#                                 break
#                         if letter == word[-1] and consecutive < 3:
#                             print(word)
#                         total += 1
# print(total-ans)
                    
                
'''
number of possible sequences is number of possible of the previous
'''