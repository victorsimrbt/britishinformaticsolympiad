'''
10

first t, 3 choices for w
'''
word = "TWOTWOTWO"
ans = 0
for idx1 in range(len(word)):
    for idx2 in range(idx1,len(word)):
        for idx3 in range(idx2,len(word)):
            if word[idx1] + word[idx2] + word[idx3] == "TWO":
                print(idx1,idx2,idx3)
                ans += 1
                

                
print(ans)
    