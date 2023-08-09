memo = {}
sum_value,idx = [int(value) for value in input().split()]
idx -= 1
value = []

def arr(n,value):
    if n in memo:
        return memo[n]
    
    if n == 1 or n == 0:
        memo[n] = value+1
        return value + 1
    
    final_value = value
    
    for i in range(n,max(n-9,0),-1):
        pos = arr(i-1,value)
        final_value += pos
        
    memo[n] = final_value
    return final_value

def construct_string(value,idx):
    sorted_dict = list(reversed([memo[key] for key in sorted(memo) if key < value]))
    for i in range(len(sorted_dict)):
        idx -= sorted_dict[i]
        if idx < 0:
            return sorted_dict[i]-abs(idx),value - (i+1)
    

arr(sum_value,0)

new_idx = idx
new_value = sum_value

values = [new_value]

#print(new_idx,new_value)
while new_value > 0:
    new_idx,new_value = construct_string(new_value,new_idx)
    #print(new_idx,new_value)
    values.append(new_value)
    
final_string = ''
for i in range(len(values)-1):
    final_string += str(values[i] - values[i+1]) + ' '
print(final_string)
