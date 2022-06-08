import numpy as np
import matplotlib.image as mpimage_of_flower

image_of_flower = mpimage_of_flower.imread('flower.jpg')

copy_of_image = image_of_flower.copy()

weighted_average_of_three_color_channels = np.array([0.1, 0.50, 0.2])
grayscale_image = copy_of_image @ weighted_average_of_three_color_channels
mpimage_of_flower.imsave('gray-flower.jpg', grayscale_image, cmap='gray')
print('Copied to black and white')