import numpy as np

distances_in_miles = np.array([1400.5, 80.2, 16.4, 0.6, 255.56, 4561.23])
distances_in_kilometers = distances_in_miles * 1.6

print(distances_in_kilometers)
# [2.240800e+03 1.283200e+02 2.624000e+01 9.600000e-01 4.088960e+02
# 7.297968e+03]

print(distances_in_kilometers.max)
# <built-in method max of numpy.ndarray object at 0x7f26069a1330>
print(distances_in_kilometers.min)
# <built-in method min of numpy.ndarray object at 0x7f26069a1330>
print(distances_in_kilometers.max())
# 7297.968
print(distances_in_kilometers.min())
# 0.96
total_distances_in_kilometers = distances_in_kilometers.sum()
print(total_distances_in_kilometers)
# 10103.184000000001
average_distances_in_kilometers = distances_in_kilometers.mean()
print(f'Mean or average of distances: {average_distances_in_kilometers}')
# Mean or average of distances: 1683.8640000000003
standard_deviation_of_distances = distances_in_kilometers.std()
print(f'Standard deviation: {standard_deviation_of_distances}')
# Standard deviation: 2628.481347548555

