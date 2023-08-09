def fix_isbn(isbn):
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
        return 0
    else:
        missing = 11* (total // 11 + 1) - total
        return int(missing/(10-missing_idx))
    
print(fix_isbn(input()))
            
    