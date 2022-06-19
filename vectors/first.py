import numpy as np
import matplotlib.pyplot as plt

# a Vector can originate anywhere, yet we can set location 
X = [-4]
Y = [-4]

# Directional vectors 
""" U = [6] # x axis, horizontal
V = [3] # y axis, vertical """
U = [-6]
V = [-3]

# Creating plot
plt.quiver(X, Y, U, V, color='b', units='xy', scale=1)
plt.title('Single Vector')

# x axis limit and y axis limit
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Show plot with grid just like a graph paper
plt.grid()
plt.show()
