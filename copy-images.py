import numpy as np
import matplotlib.image as mpimage_of_flower

image_of_flower = mpimage_of_flower.imread('flower.jpg')

copy_of_image = image_of_flower.copy()
copy_of_image[:, :, :2] = 0
mpimage_of_flower.imsave('flower-one.jpg', copy_of_image)
print('Copied.')