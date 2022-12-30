# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:25:02 2022

@author: B3ar
"""

import numpy as np
import random as rn
import matplotlib as plt


x = np.array([12.7,73,98,23,56,73,23,12])
print(x)

y = np.random.normal(size = 10)
print(y)

z = np.random.normal(100,20000, size = (2,4))
print(z)

points =np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)

z= np.sqrt((xs**2) + (ys**2))

plt.imshow(z, cmap=plt.cm.Reds)
plt.colorbar()
plt.show()
