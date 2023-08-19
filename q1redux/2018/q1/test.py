import math
import time
import random
def roundup(num):
    num = str(num)
    num,dec = num.split(".")
    dec = list(dec)
    if len(dec) >= 3:
        if int(dec[2]) > 0:
            dec[1] = str(int(dec[1])+1)
        dec = ''.join(dec)
        return float(num+"."+dec[:2])
    return float(num+"."+''.join(dec))

for i in range(100):
    # for r in range(100):
    debt = 100
    i_rate,r_rate = random.randint(1,100),random.randint(1,100)
    print("Interest Rate: {}, Repayment Rate: {}".format(i_rate,r_rate))
    i_rate /= 100
    r_rate /= 100

    ans = 0

    while debt > 0:
        debt *= (1+i_rate)
        debt = roundup(debt)
        repay = max(roundup(r_rate * debt),50)
        repay = min(repay,debt)
        ans += repay
        debt -= repay
        print(repay,debt)
        
    print(ans)
    print()
    time.sleep(1)

# print(roundup(float(input())))