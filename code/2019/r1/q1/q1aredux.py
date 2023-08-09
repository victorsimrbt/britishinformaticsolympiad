
def add_layer(nums):
    new_nums = []
    for val in nums:
        for x in range(10):
            new_nums.append([x] + val + [x])
    return new_nums
digits = 10
palindromes = [[i] for i in range(10)]

for x in range(digits):
    palindromes = add_layer(palindromes)
    # print(palindromes)
    