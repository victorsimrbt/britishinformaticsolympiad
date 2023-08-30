a,b = map(int,input().split())
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
print("{}:{}".format(hour,minute))