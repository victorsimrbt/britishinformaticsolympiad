clrs = 'RGB'
convert = {
    "RB" : "G",
    "BR" : "G",
    "GB" : "R",
    "BG" : "R",
    "GR" : "B",
    "RG" : "B",
    "BB" : "B",
    "RR" : "R",
    "GG" : "G"
}
def next(row):
    if len(row) == 1:
        return row
    new_row = ''
    for i in range(len(row)-1):
        double = row[i] + row[i+1]
        new_row += convert[double]
    return new_row
for clr_1 in clrs:
    for clr_2 in clrs:
        for clr_3 in clrs:
            for clr_4 in clrs:
                for clr_5 in clrs:
                    for clr_6 in clrs:
                        for clr_7 in clrs:
                            for clr_8 in clrs:
                                for clr_9 in clrs:
                                    string = clr_1+clr_2+clr_3+clr_4+clr_5+clr_6+clr_7+clr_8+clr_9
                                    if next(string) == "RRGBRGBB":
                                        print(string)
                                
'''
3
RRRBBGGRG
GBGGRRBBB
BGBRGBRGR
'''