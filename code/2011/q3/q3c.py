'''
38 digits
'''
import time
ten_combos = [[i,10-i] for i in range(1,10)]
digits = 1

total = 0
while True and digits < 100:
    digit_size = len(ten_combos)**(digits//2)
    total += digit_size
    digits += 1
    if total >  1000000000000000000:
        print("ANSWR",digits)
        break
    print(total)
    time.sleep(0.1)
    