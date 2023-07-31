import time
row = input()
new_row = ''

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

while True:
    row = next(row)
    if len(row) == 1:
        break
print(row)
        
    

    
    