import itertools
pairs = []
for num1 in range(10):
    for num2 in range(10):
        pairs.append([str(num1)+str(num2)])

def valid(date):
    string = ''.join(date)
    true_count = {}
    for char in string:
        if char in true_count:
            true_count[char] += 1
        else:
            true_count[char] = 1
    
    construct_count = {}
    for pair in date:
        count,digit = pair
        if digit in construct_count:
            return False
        construct_count[digit] = int(count)
    # print(construct_count,true_count)
    return construct_count == true_count

def pairify(string):
    pairs = []
    for i in range(len(string)//2):
        pairs.append(string[i*2:i*2+2])
    return pairs
# date = pairify("10143133")
length = 1
while length < 6:
    print("Length: {}".format(length))
    dates = itertools.permutations(pairs,length)
    print(len(list(dates)))
    # print(list(dates))
    for date in dates:
        date = [term[0] for term in date]
        # print(date)
        if valid(date):
            print(''.join(date))
    length += 1
    
    
# print(valid(date))