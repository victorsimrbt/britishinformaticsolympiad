'''
0 8 9 16
'''
for i in range(20):
    a,b = 0,i
    time1,time2 = 0,0
    while True:
        time1 += 60
        time2 += 60
        time1 += a
        time2 += b
        if (time1 % 1440) == (time2%1440):
            break
    # print(time1)
    hour = str(time1%1440//60)
    if len(hour) == 1:
        hour = "0" + hour
    minute = str(time2%1440%60)
    if len(minute) == 1:
        minute = "0" + minute
    print("{}: {}:{}".format(i,hour,minute))