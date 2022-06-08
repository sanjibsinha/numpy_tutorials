import numpy as np
import matplotlib.image as mpimage_of_flower

image_of_flower = mpimage_of_flower.imread('flower.jpg')
print(type(image_of_flower))
print(image_of_flower.shape)
# (452, 640, 3)