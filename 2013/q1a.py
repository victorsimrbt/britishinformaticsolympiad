
clock_1,clock_2 = [int(val) for val in input().split()]

def minute2string(minutes):
    hours = [str(minutes // 60) if minutes // 60 >= 10 else "0" + str(minutes // 60)]
    minutes = [str(minutes % 60) if minutes % 60 >= 10 else "0" + str(minutes % 60)]
    return hours[0]+':'+minutes[0]

for i in range(1,10000):
    if (clock_1*i+i)%1440 == (clock_2*i+i)%1440:
        print(i)
        clock_value = (clock_1*i+i*60)%1440
        print(minute2string(clock_value))
        break