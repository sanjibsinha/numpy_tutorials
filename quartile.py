import numpy

values = [13,21,21,40,42,49,55,76, 85]

quantile_values = numpy.quantile(values, [0,0.25,0.5,0.75,1])

print(f'Quantile values: {quantile_values}')

# Quantile values: [13. 21. 42. 55. 85.]