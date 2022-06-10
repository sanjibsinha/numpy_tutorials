import numpy as np
data = list(range(55, 75, 90))
print(data)
# [20, 30, 40, 50, 60, 70, 80, 90]

Q1 = np.quantile(data, 0.25)
Q2 = np.quantile(data, 0.50)
Q3 = np.quantile(data, 0.75)

print("Quartile 1 : ", Q1)
print("Quartile 2 : ", Q2)
print("Quartile 3 : ", Q3)

'''
Quartile 1 :  37.5
Quartile 2 :  55.0
Quartile 3 :  72.5
'''

def QuartileDeviation(a, b):
    return (a - b)/2
print(f'Quartile Deviation: {QuartileDeviation(Q3, Q1)})')

# Quartile Deviation: 17.5)