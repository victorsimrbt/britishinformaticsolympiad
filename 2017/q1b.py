'''
3 rows 

RRRBBGGRG
GBGGRRBBB
BGBRGBRGR

'''
block = "RGB"
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


for val1 in block:
    for val2 in block:
        for val3 in block:
            for val4 in block:
                for val5 in block:
                    for val6 in block:
                        for val7 in block:
                            for val8 in block:
                                for val9 in block:
                                    row = val1+val2+val3+val4+val5+val6+val7+val8+val9
                                    orig = row
                                    new_row = ''
                                    for i in range(len(row)-1):
                                        duo = row[i:i+2]
                                        new_row += translate[duo]
                                    row = new_row
                                    if row == "RRGBRGBB":
                                        print(orig)
                                    # print(row)
                                    