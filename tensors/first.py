import numpy as np
import matplotlib.pyplot as plt

tensor = np.array([
    [[111, 52, 3], [74, 5, 666], [7, 88, 19]],
    [[11, 912, 813], [414, 158, 16], [517, 718, 19]],
    [[21, 228, 123], [242, 25, 126], [217, 280, 29]],
])

print(tensor)

'''
[[[111  52   3]
  [ 74   5 666]
  [  7  88  19]]

 [[ 11 912 813]
  [414 158  16]
  [517 718  19]]

 [[ 21 228 123]
  [242  25 126]
  [217 280  29]]]
'''

plt.imshow(tensor, interpolation='nearest')
plt.show()