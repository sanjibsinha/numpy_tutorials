import numpy as np

two_dimensional_array = np.array([
    [10, 257, 3, 45, 185, 366],
    [110, 127, 53, 415, 15, 66],
    [104, 207, 93, 45, 815, 866],
    [710, 270, 83, 145, 115, 66]
])
# print(two_dimensional_array)

print(two_dimensional_array.shape)

# (4, 6)

changing_column_to_row = two_dimensional_array.reshape(6, 4)
print(changing_column_to_row)

'''
[[ 10 257   3  45]
 [185 366 110 127]
 [ 53 415  15  66]
 [104 207  93  45]
 [815 866 710 270]
 [ 83 145 115  66]]
'''

print(changing_column_to_row.shape)

# (6, 4)