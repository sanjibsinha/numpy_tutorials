import numpy as np

values = [40, 48, 56, 62, 75, 85, 85, 90, 99]

percentile_values = np.percentile(values, 65)

print(f'Percentile Values: {percentile_values}')

# Percentile Values: 85.0