row = input()

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
    
print(row)