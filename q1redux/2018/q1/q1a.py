import math
def roundup(num):
    num = str(num)
    if not "." in num:
        return float(num)
    num,dec = num.split(".")
    dec = list(dec)
    if len(dec) >= 3:
        if int(dec[2]) > 0:
            dec[1] = str(int(dec[1])+1)
        dec = ''.join(dec)
        return float(num+"."+dec[:2])
    return float(num+"."+''.join(dec))

debt = 100
i_rate,r_rate = map(int,input().split())
i_rate /= 100
r_rate /= 100

ans = 0

while debt > 0:
    # print("BEFORE",debt)
    debt *= (1+i_rate)
    # print(round(debt-int(debt),4))
    # debt = int(debt) + roundup(round(debt-int(debt),4))
    debt = roundup(debt)
    # print(debt)
    repay = r_rate * debt
    # repay = int(repay) + roundup(round(repay-int(repay),4))
    repay = roundup(repay)
    repay = max(repay,50)
    repay = min(repay,debt)
    ans += repay
    debt -= roundup(repay)
    print(debt)
    debt = roundup(debt)
    
    # payment += 1
    print(repay,debt)
    # print()
    
print(round(ans,2))

# print(roundup(float(input())))