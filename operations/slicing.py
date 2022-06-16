import numpy as np

lists = [5, 6, 9, 8]
#        0  1  2  3
#        -3 -2 -1 0
print(lists[:2]) # it removess from index 2
# [5, 6]
print(lists[1:3]) # it starts from index 1, removess from index 3
# [6, 9]
print(lists[-3:]) # it removess from index 0 which is -3
# [6, 9, 8] 
np_array = np.array([5, 6, 9, 8])
print(np_array[:2])
# [5, 6]
print(np_array[1:3])
# [6, 9]
print(np_array[-3:])
# [6, 9, 8] 

np_arrays = np.array([[11, 2, 355, 4], [5, 60, 17, 78], [9, 10, 111, 512]])

print(np_arrays < 100)
'''
[[ True  True False  True]
 [ True  True  True  True]
 [ True  True False False]]
'''
print(np_arrays[np_arrays < 100])
# [11  2  4  5 60 17 78  9 10]
print(np_arrays[np_arrays >= 10])
# [ 11 355  60  17  78  10 111 512]
print(np_arrays[(np_arrays >= 100) & (np_arrays <= 300 )])