import random
def all_before(num):
    if len(num) % 2 == 0:
        first_half = num[:len(num)//2]
        second_half = num[len(num)//2:]
    else:
        # print(num)
        first_half = str(num[:len(num)//2])
        second_half = num[len(num)//2+1:]
    first_half = ''.join(reversed(first_half))
    # print(first_half,second_half)
    for i in range(len(str(first_half))):
        # ! check if every character in first string is greater than or equal to second string
        if second_half[i] > first_half[i]:
            return False
        if first_half[i] > second_half[i]:
            return True
    if first_half == second_half:
        return False
    return True

def next_palindrome(num):
    if str(num).count("9") == len(str(num)):
        return str(num+2)
    if num < 9:
        return str(num+1)
    if num == 9:
        return "11"
    '''
    even vs odd length
    
    if even:
        if all number in second are less than first half:
            12341111 -> 12344321
            12344320
            
            1234
        12344321
        
        otherwise:
            12344321 -> 12355321
            12345678 -> 12355321
            12399321 -> 12400421
            
            1041
            add 1 to the last num in first half and carry it over
            copy to both sides
    
    if odd:
        if all number in second are less than first half:
            copy across
        otherwise:
            10301 - > 10401
            add 1 to the middle number and carry over then copy left onto right
            10321
        
    '''
    num = str(num)
    if len(num) % 2 == 0:
        first_half = num[:len(num)//2]
        if all_before(num):
            # print("YES")
            ans = first_half + ''.join(reversed(first_half))
            # return ans
        else:
            # print("NO")
            # print(num,first_half)
            first_half = int(first_half) + 1
            first_half = str(first_half)
            ans = first_half + ''.join(reversed(first_half))
            # return ans
    else:
        first_half = num[:len(num)//2]
        # second_half = num[len(num)//2+1:]
        # print(first_half,second_half)
        if all_before(num):
            
            ans = first_half + num[len(num)//2] + ''.join(reversed(first_half))
            # print("YES")
        else:
            first_half = str(int(num[:len(num)//2+1]) + 1)
            ans = first_half + ''.join(reversed(first_half[:-1]))
            # print("NO")
            
        # first_half = str(int(first_half)+1)
        # ans = first_half + ''.join(reversed(first_half[:-1]))
        # ans = None
    return ans
    
def naive(num):
    while True:
        num += 1
        if list(reversed(str(num))) == list(str(num)):
            # print(list(reversed(str(num))),list(str(num)))
            return str(num)
            # break


n = int(input())
print(next_palindrome(n))
# # print(next_palindrome(n),naive(n))
# # exit()
# for n in range(1,20000):
#     # print(n)
#     # print(next_palindrome(n),naive(n))
#     if next_palindrome(n) != naive(n):
#         print("WRONG",n,next_palindrome(n),naive(n))
#         exit()
#     # print("NAIVE: {}".format(naive(n)))