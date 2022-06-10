import numpy as np

one_dimension = np.arange(8)
print(one_dimension)
# [0 1 2 3 4 5 6 7]

first_two_dimension = one_dimension.reshape(2, 4)
print(first_two_dimension)
'''
[[0 1 2 3]
 [4 5 6 7]]
'''

second_two_dimension = one_dimension.reshape(4, 2)
print(second_two_dimension)
'''
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
'''
# comparison operator
less_four = first_two_dimension[first_two_dimension < 4]
print(less_four)
# [0 1 2 3]

four_and_up = first_two_dimension[first_two_dimension >= 4]
print(four_and_up)
# [4 5 6 7]

even_numbers = first_two_dimension[first_two_dimension % 2 == 0]
print(even_numbers)
# [0 2 4 6]

odd_numbers = first_two_dimension[first_two_dimension % 2 != 0]
print(odd_numbers)
# [1 3 5 7]

# logical operator
less_and_greater = first_two_dimension[(first_two_dimension < 7) & (first_two_dimension > 2)]
print(less_and_greater)
# [3 4 5 6]