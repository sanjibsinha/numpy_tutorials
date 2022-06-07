import numpy as np

company_profits = np.arange(21, dtype=np.int64).reshape(3, 7)

company_profits[1:, ::2] = -1

print(company_profits)

'''
[                
                 J  F  M  A  M  J  J
                ---------------------
 First Month   [ 0  1  2  3  4  5  6]
 Second Month  [-1  8 -1 10 -1 12 -1]
 Third Month   [-1 15 -1 17 -1 19 -1]
 
]
'''
max_profit_month_wise = company_profits.max(axis=1)
print(max_profit_month_wise)

'''
[ 
First Month --  6 
Second Month --  12 
Third Month --   19
                    ]
'''

