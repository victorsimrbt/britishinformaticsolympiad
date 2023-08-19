import math

interest,repayment = [float(val)/100 for val in input().split()]

repaid = 0.0
debt = 100.0
def threedp(n):
    return n

while debt > 0:
    debt *= (1+interest)
    debt = round(debt,5)
    debt = math.ceil(round(threedp(debt)*100,5))/100
    repay = max(repayment * debt,50.0)
    repay = min(repay,debt)
    repay = round(repay,5)
    repay = math.ceil(round(threedp(repay)*100,5))/100
    debt -= repay
    debt = round(debt,5)
    repaid += repay
    repaid = round(repaid,5)
    
print(repaid)