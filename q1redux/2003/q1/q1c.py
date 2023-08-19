'''
3201014525

2301014525 0 1 (1)
1320104525 0 5
3200114525 2 4
3200114525 3 4
3204101525 3 6
3202101455 3 8
3201501425 4 7
'''
isbn = "3201014525"

def valid(isbn):
    total = 0
    for i in range(len(isbn)):
        val = isbn[i]
        if val == "?":
            missing_idx = i
        else:
            if val == "X":
                val = 10
            total += (10-i) * int(val)
            # print(10-i,val,total)
    # print(total)
    # ! next_multiple of 11
    if total % 11 == 0:
        return True
    else:
        return False

for idx1 in range(len(isbn)):
    for idx2 in range(idx1,len(isbn)):
        test_isbn = list(isbn)[:]
        # print(idx1,idx2)
        temp = test_isbn[idx1]
        test_isbn[idx1] = test_isbn[idx2]
        test_isbn[idx2] = temp
        # print(''.join(test_isbn))
        if valid(test_isbn):
            print(''.join(test_isbn),idx1,idx2)