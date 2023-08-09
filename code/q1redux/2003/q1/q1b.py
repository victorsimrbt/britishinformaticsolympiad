'''
3540678654
9514451570 

2/2
'''
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
    print(total)
    # ! next_multiple of 11
    if total % 11 == 0:
        return True
    else:
        return False
    
isbns = ["0972311900", "3540678654", "9514451570", "013674409X"]
for isbn in isbns:
    print(valid(isbn))
    print()