import numpy as np
an_array = np.array([
    [1, 1], 
    [0, 1]
])
another_array = np.array([
    [2, 0], 
    [3, 4]
])
'''
Matrix
a @ b
np.dot(a,b)
a[0, 0]*b[0, 0] + a[0, 1]*b[1, 0] | a[0, 0]*b[0, 1] + a[0, 1]*b[1, 1]
----------------------------------|----------------------------------
a[1, 0]*b[0, 0] + a[1, 1]*b[1, 0] | a[1, 0]*b[0, 1] + a[1, 1]*b[1, 1]

1*2 + 1*3 | 1*0 + 1*4
----------|----------
2*2 + 1*3 | 0*2 + 1*4

'''

# element wise
print(an_array * another_array)
'''
[[2 0]
 [0 4]]
'''
# matrix multiplication or product
print(an_array @ another_array)
'''
[[5 4]
 [3 4]]
'''