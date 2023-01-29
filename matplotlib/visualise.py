# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 21:24:44 2022

@author: B3ar
"""

import matplotlib.pyplot as plt
import numpy as np



# Create an array
points = np.arange(-5, 5, 0.01)

# Make a meshgrid
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)

# Display the image on the axes
plt.imshow(z, cmap=plt.cm.Reds)

# Draw a color bar
plt.colorbar()

# Show the plot
plt.show()