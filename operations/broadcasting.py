import numpy as np

distances_in_miles = np.array([14.5, 80.2, 6.4, 0.6, 25.56])
distances_in_kilometers = distances_in_miles * 1.6

print(distances_in_kilometers)
# [ 23.2   128.32   10.24    0.96   40.896]

print(distances_in_kilometers.max)
# <built-in method max of numpy.ndarray object at 0x7fc0eed1b330>
print(distances_in_kilometers.min)
# <built-in method min of numpy.ndarray object at 0x7fc0eed1b330>
print(distances_in_kilometers.max())
# 128.32000000000002
print(distances_in_kilometers.min())
# 0.96
total_distances_in_kilometers = distances_in_kilometers.sum()
print(total_distances_in_kilometers)
# 203.61600000000004
average_distances_in_kilometers = distances_in_kilometers.mean()
print(f'Mean or average of distances: {average_distances_in_kilometers}')
# Mean or average of distances: 40.723200000000006
standard_deviation_of_distances = distances_in_kilometers.std()
print(f'Standard deviation: {standard_deviation_of_distances}')
# Standard deviation: 45.80530389550975

