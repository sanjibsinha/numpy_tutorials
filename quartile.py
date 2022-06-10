import numpy as np

values = [70, 80, 85, 90, 95]

quantile_values = np.quantile(values, [0,0.25,0.5,0.75,1])

print(f'Quantile values: {quantile_values}')

# Quantile values: [70. 80. 85. 90. 95.]

print(f'Median Value: {np.median(quantile_values)}')

# Median Value: 85.0