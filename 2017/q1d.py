import random
'''
8,10,12
'''
for i in range(4,100):
    print(i)
    for x in range(1000):
        row = "R"
        for _ in range(i-2):
            string = "RGB"
            row += string[random.randint(0,2)]
            # print(row)
        # print("ROW",row)
        # print("ROW",row)
        row += "G"
        translate = {
        "RR" : "R",
        "RG" : "B",
        "RB" : "G",
        "GG" : "G",
        "GR" : "B",
        "GB" : "R",
        "BB" : "B",
        "BG" : "R",
        "BR" : "G"
    }

        while len(row) != 1:
            new_row = ''
            for i in range(len(row)-1):
                duo = row[i:i+2]
                new_row += translate[duo]
            row = new_row
        if x == 0:
            final_val = row
        if row == final_val:
            pass
        else:
            print("FAIL")
            print()
            break
    