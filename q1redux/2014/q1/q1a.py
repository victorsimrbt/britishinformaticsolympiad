lucky = [i for i in range(1,10100) if i % 2 == 1]
def remove(lucky,n):
    new_lucky = []
    for i in range(len(lucky)):
        if (i+1) % n == 0 and i != 0:
            pass
        else:
            new_lucky.append(lucky[i])
    return new_lucky

def ans(n):
    for i in range(len(lucky)):
        if lucky[i] >= n:
            low = lucky[i-1]
            break
    for i in range(len(lucky)):
        if lucky[i] > n:
            high = lucky[i]
            break
    
    return str(low) + ' ' + str(high)

val_idx = 1
# print(lucky)
while val_idx < len(lucky):
    remove_val = lucky[val_idx]
    lucky = remove(lucky,remove_val)
    val_idx += 1
# print(lucky[-10:])
print(ans(int(input())))
# print(lucky)
# print(lucky)

