import numpy as np

one_dimensional_array = np.array([10, 27, 3, 45, 15, 66])

print(one_dimensional_array)
# [10 27  3 45 15 66]

print(one_dimensional_array[0]) # 10
print(one_dimensional_array[3]) # 45

two_dimensional_array = np.array([
    [10, 257, 3, 45, 185, 366],
    [110, 127, 53, 415, 15, 66],
    [104, 207, 93, 45, 815, 866],
    [710, 270, 83, 145, 115, 66]
])
print(two_dimensional_array)

'''
[[ 10 257   3  45 185 366]
 [110 127  53 415  15  66]
 [104 207  93  45 815 866]
 [710 270  83 145 115  66]]
'''

print(two_dimensional_array[2])
# [104 207  93  45 815 866]
print(two_dimensional_array[2][3])
# 45

