import numpy

values = [13,21,21,40,42,48,55,72, 85]

percentile_values = numpy.percentile(values, 65)

print(f'Percentile Values: {percentile_values}')

# Percentile Values: 49.4