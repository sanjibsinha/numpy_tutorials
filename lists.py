import numpy as np


a_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# sum_of_rows = list(map(sum, a_list))
sum_of_rows = [ sum(x) for x in a_list ]
print(sum_of_rows)
# [6, 15, 24]

sum_of_columns = [ sum(x) for x in zip(*a_list) ]
print(sum_of_columns)
# [12, 15, 18]

np_array = np.array(a_list)

column_axis = np_array.sum(axis=0)
print(column_axis)
# [12, 15, 18]

row_axis = np_array.sum(axis=1)
print(row_axis)
# [ 6 15 24]