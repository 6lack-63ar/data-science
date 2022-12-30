# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 02:11:24 2022

@author: B3ar
"""
import numpy as np
#addition of elemnt wise addition
A = np.array([[1,1,8],[0,1,9],[9,0,8]])
B = np.array([[2,0,0],[3,4,9],[7,8,9]])

def add(a,b):#same as subtraction
    c = A+B
    print("the sum of matrix \nA=",A,"and matrix \nB=",B,"is :")
    print(c,"\n")
add(A,B)

def mult(a,b):#SAME AS DIVISION
    c= A*B
    print("the multiple of matrix \nA=",A,"and matrix \nB=",B,"is :")
    print(c)
mult(A,B)