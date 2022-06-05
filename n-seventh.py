from re import A
import numpy as np

np_array = np.arange(5)
# print(np_array) # [0 1 2 3 4]

np_array = np.linspace(1, 5, 4)

# print(np_array) # [1.         2.33333333 3.66666667 5.        ]

np_array = np.empty([2, 2], dtype=int)
# print(np_array)
'''
[[1.31467864e-316 0.00000000e+000]
 [9.13544126e+242 1.05164878e-153]]
'''
np_array = np.empty([2, 2], dtype=int)
# print(np_array)

'''
[[4607182418800017408 4612436618365282986]
 [4615439018116863317 4617315517961601024]]
'''

np_array = np.empty_like(np.linspace(1, 5, 4), dtype=int)
# return an array with the same shape and size
# print(np_array)
'''
[       18033760               0 140170445206448 140170536619824]
'''

np_array = np.identity(3) # returning an identical array
# print(np_array)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
np_array = np.arange(100)# 
# print(np_array)
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99]
'''

# print(np_array.reshape(4, 25))
'''
[[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
  24]
 [25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48
  49]
 [50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73
  74]
 [75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98
  99]]
'''
# print(np_array.ravel())
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99]
'''

two_dimensional_array = [
    [1, 5, 9],
    [3, 5, 7],
    [2, 5, 8]
]
np_array = np.array(two_dimensional_array)
# print(np_array)
'''
[[1 5 9]
 [3 5 7]
 [2 5 8]]
'''
column_axis = np_array.sum(axis=0)
# print(column_axis)
# [ 6 15 24]
row_axis = np_array.sum(axis=1)
# print(row_axis)
# [15 15 15]

keyboard = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

keyboard_layout = np.array(keyboard)
column_axis = keyboard_layout.sum(axis=0)
# print(column_axis)
'''
[12 15 18]
'''

row_axis = keyboard_layout.sum(axis=1)
# print(row_axis)
'''
[24 15  6]
'''

company_profits = [
    # rows -> months
    # columns -> years                 
        
    [123, 654, 789],
    [214, 789, 632], 
    [987, 456, 987]
]

company_profits_array = np.array(company_profits)
# print(company_profits_array)
first_year_first_month_profit = company_profits_array[0][0]
# print(first_year_first_month_profit) # 123
first_year_second_month_profit = company_profits_array[0][1]
# print(first_year_second_month_profit) # 654
profits_year_wise = company_profits_array.sum(axis=0)
print(profits_year_wise)
# [1324 1899 2408]
first_year_profits = profits_year_wise[0]
print(first_year_profits) # 1324
profits_month_wise = company_profits_array.sum(axis=1)
print(profits_month_wise)
# [1566 1635 2430]
third_month_wise_profits = profits_month_wise[2]
print(third_month_wise_profits) # 2430
