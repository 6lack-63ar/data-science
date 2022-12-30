# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:47:31 2022

@author: B3ar
"""

import numpy as np

array1 = [12,12,4,2,5,356,5643,345,23,12,4,23,6,3,76,23412,768,2323,768,2,6123,5,7]

print(type(array1))
array2= np.array(array1)

print(type(array2))

weights = np.array([[12,55],[34,34],[56,86],[23,85],[25,8],[25,85],[26,74],[37,89]])
print(type(weights))

print(weights)
print(weights.size,"is the size of the array \n")
print(weights.shape,"is the shape of the array\n")
print(weights.dtype,"is the dtype of the array\n")
print(weights.ndim,"is the dimension of the array\n")


heights= np.linspace(start=100,stop=1000,num=50)
print(heights,"\n")

breadth= np.full((6,5),6)
print(breadth,"\n")#print a value of the n*n array filled with value 6





peights = np.arange(start = 100,stop=1000,step=100,dtype="int32")
print(peights)#outputs one dimenion array

#peights.reshape(5,4,2)
#print(aeights)
#check this out not working

#wieghts_flat = np.flatten(weights)#error check
#print(wieghts_flat)

#(arr1,arr2)
#equal
#not_equa
#greater(same as less)
#not_greater

#generating random matrices
# to be continued

tights = np.random.random(15)
print(tights)