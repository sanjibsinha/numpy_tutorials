import numpy as np 
import matplotlib.pyplot as plt

first = np.array([5, 7])
second = np.array([2, 4])

# PLotting addition of two arrays or single vectors

sum_of_two_arrays = np.add(first, second)

print(sum_of_two_arrays)

plt.plot(first) 
plt.plot(second) 
plt.plot(sum_of_two_arrays) 
plt.plot(np.array([2, 7]))

# Add Title

plt.title("Matplotlib PLotting NumPy Arrays") 

# Add Axes Labels

plt.xlabel("x axis") 
plt.ylabel("y axis") 

# x axis limit and y axis limit
""" plt.xlim(0, 6)
plt.ylim(0, 15)

# Show plot with grid just like a graph paper
plt.grid() """

# Display

plt.show()