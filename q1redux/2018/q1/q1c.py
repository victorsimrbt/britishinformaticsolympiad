import math
import time
import random
'''
11189.66
'''
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

payments = 0
maximum = 0
for i in range(101):
    for r in range(101):
        # payments = 0
    # for r in range(100):
        debt = 100
        i_rate,r_rate = i,r
        # print("Interest Rate: {}, Repayment Rate: {}".format(i_rate,r_rate))
        i_rate /= 100
        r_rate /= 100

        ans = 0
        payment = 0
        while debt > 0 and payment <= 500:
            # print("BEFORE",debt)
            debt *= (1+i_rate)
            # print(round(debt-int(debt),4))
            debt = int(debt) + roundup(round(debt-int(debt),4))
            # debt = roundup(debt)
            # print(debt)
            repay = r_rate * debt
            repay = int(repay) + roundup(round(repay-int(repay),4))
            repay = max(repay,50)
            repay = min(repay,debt)
            ans += repay
            debt -= repay
            payment += 1
            # print(repay,debt,debt/repay)
            # print()
        if payment < 500:
            # print(ans)
            # print()
            if ans > maximum:
                print(i,r,ans)
                maximum = ans
            # maximum = max(maximum,ans)
        # except:
        #     print("Overflow")
                    
        # time.sleep(1)

# print(roundup(float(input())))
print(maximum)