import numpy as np

first = np.array([2, 3, 444, 5, 6], np.int8)

print(first)
print(first.shape)
print(first.dtype)
print(first.size)

'''
[  2   3 -68   5   6]
(5,)
int8
5

int8	Byte (-128 to 127)
int16	Integer (-32768 to 32767)
int32	Integer (-2147483648 to 2147483647)
int64	Integer (-9223372036854775808 to 9223372036854775807)
'''