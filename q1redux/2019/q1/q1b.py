'''
10000000000000000001
'''
prev = 0
big_diff = 0
for i1 in range(1,10):
    print(i1)
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                for i5 in range(10):
                    for i6 in range(10):
                        for i7 in range(10):
                            for i8 in range(10):
                                print(big_diff)
                                for i9 in range(10):
                                    for i10 in range(10):
                                        num = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]
                                        num = ''.join([str(val) for val in num])
                                        num = int(num + ''.join(reversed(num)))
                                        big_diff = max(big_diff,num-prev)
                                        prev = num
                                        # print(big)
                                        
                                        