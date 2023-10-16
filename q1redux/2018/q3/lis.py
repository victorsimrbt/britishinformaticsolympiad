def lis(a):
    tails = [0] * (len(a)+1)
    tails[0] = "Z"
    length = 1
    for i in range(len(a)):
        print("LETTER",a[i])
        update = -1
        for j in range(length):
            print(j)
            if (tails[j] > a[j]):
                update = j
                break
        print(update)
        if update == -1 and a[i] > tails[0]:
            length += 1
            tails[length-1] = a[i]
        else:
            tails[update] = a[i]
        print(tails)
    return length-1

print(lis("ACBDEAAAA"))
    