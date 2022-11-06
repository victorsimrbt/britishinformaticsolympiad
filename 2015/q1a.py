blocks = [[]]
def block_palindrome(string):
    block_possibilities = 0
    for i in range(1,len(string)//2+1):
        if string[:i] == string[-i:]:
            start_block = string[:i]
            end_block = string[-i:]
            #print("OPERATING ON",string,start_block,end_block) 
            block_possibilities += block_palindrome(string[i:-i])
            block_possibilities += 1
    return block_possibilities


print(block_palindrome(input()))
        