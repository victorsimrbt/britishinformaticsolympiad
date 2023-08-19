'''
every square is connected

so corner squares cannot be 1,2

top corner cannot be 1,2,3,4,

side_squares can only be 1 or 2 or 6 or 5

1 (all small diamonds)
+ 2 (4 by 2 loops) (vertical and horizontal)
+ 4 (1(4 by 2) and 2(2 by 2) diamonds)
+ 4 (2 by 2 diamond with the l shape shape)

= 11
'''
import itertools
x = [1,2,3,4,5,6]
row_configs = [p for p in itertools.product(x, repeat=4)]
print(len(row_configs))