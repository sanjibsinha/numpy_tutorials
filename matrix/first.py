import numpy as np

a = np.array([
    [1, 0], 
    [0, 1]
])

b = np.array([
    [4, 1], 
    [2, 2]
])

print(np.dot(a, b))
print(a @ b)
'''
a[0, 0]*b[0, 0] | a[1, 0]*b[1, 0]
----------------|----------------                  
a[0, 1]*b[0, 1] | a[1, 1]*b[1, 1]
                



[[4 1]
 [2 2]]
'''