'''
digits last
go from the middle out
change from left to right

for any two numbers:
    if left is smaller:
        left = left + 1
        right = left
    if left is larger:
        left = left
        right = left

if it is a palindrome:
    add 1 to both values from the centre
    
790
??A??

100
101
102
103
104
105
106
107
108
109
110

899

879
'''

# num = list(map(int,input()))

def next_palindrome(num):
    ans = num[:]
    # print(reversed(ans),ans)
    if len(num) % 2 != 0:
        middle_idx = len(num)//2
        left_idx = middle_idx -1
        right_idx = middle_idx + 1
        
        if list(reversed(ans)) == ans:
            # print("PALINDROME")
            if ans[middle_idx] != 9:
                ans[middle_idx] += 1
                return ans
            # print("MIDDLE ONE")
            while left_idx >= 0:
                if ans[left_idx] != 9:
                    ans[left_idx] += 1
                    ans[right_idx] += 1
                    return ans
                left_idx -= 1
                right_idx += 1
            # print("MUST BE ALL 9s")
            ans = int(''.join([str(val) for val in ans]))
            ans += 1
            ans = list(str(ans))
            return ans
        # big = True
        # if ans[middle_idx] != 9:
        #     ans[middle_idx] += 1
        #     big = True
        # else:
        #     ans[left_idx] += 1
        #     ans[middle_idx] = 0
        #     ans[right_idx] = ans[left_idx]
        #     big = False
        big = False
    else:
        middle_idx = len(num)//2
        left_idx = middle_idx -1
        right_idx = middle_idx
        
        if list(reversed(ans)) == ans:
            # if ans[middle_idx] != 9:
            #     ans[middle_idx] += 1
            #     return ans
            while left_idx >= 0:
                if ans[left_idx] != 9:
                    ans[left_idx] += 1
                    ans[right_idx] += 1
                    return ans
                left_idx -= 1
                right_idx += 1
            ans = int(''.join([str(val) for val in ans]))
            ans += 2
            ans = list(str(ans))
            return ans
        big = False


    # print(left_idx,right_idx)
    while left_idx >= 0:
        
        left = ans[left_idx]
        right = ans[right_idx]
        # print(left,right)
        
        if left < right:
            if not(big):
                left += 1
                right = left
            else:
                right = left
        
        if left > right:
            right = left
            big = True
        ans[left_idx] = left
        ans[right_idx] = right
        
        left_idx -= 1
        right_idx += 1
    return ans

num = list(map(int,input()))
ans = [str(val) for val in next_palindrome(num)]
print(''.join(ans))
# # # exit()
# for x in range(1000):
#     num = list(map(int,str(x)))
#     ans = [str(val) for val in next_palindrome(num)]
#     print(x,''.join(ans))

