
# coding: utf-8

# Task:Approximation of functions

import numpy as np
import scipy as sp
import matplotlib as mp
import math
import scipy.linalg
from matplotlib import pylab as plt


# Defining Functions
def f(x):
    f = math.sin(x/5.0)*math.exp(x/10.0)+5*math.exp(-x/2.0)
    return f


# Formation of a system of linear equations (matrix of coefficients "a" and free vector "c") 
# for a polynomial of the first degree that coincides with the function "f" at points 1 and 15. Solution of the system and its graph.
a = np.array([[1,1],[1,15]])
b = np.array([f(1), f(15)])
solution = sp.linalg.solve(a,b)
x = np.arange(1, 15, 0.1)
y = solution[0] + x * solution[1]
plt.plot(x, y)
plt.show()

# Formation of a system of linear equations (matrix of coefficients "a" and free vector "c") 
#for a polynomial of the second degree that coincides with the function "f" at points 1 and 15. Solution of the system and its graph.
a = np.array([[1,1,1],[1,8,64],[1,15, 225]])
b = np.array([f(1), f(8), f(15)])
solution = sp.linalg.solve(a,b)
x = np.arange(1, 15, 0.1)
y = solution[0] + x * solution[1] + x**2 * solution[2]
plt.plot(x, y)
plt.show()

# Formation of a system of linear equations (matrix of coefficients "a" and free vector "c") 
#for a polynomial of the third degree that coincides with the function "f" at points 1 and 15. Solution of the system and its graph.
a = np.array([[1,1,1,1],[1,4,16,64],[1,10, 100, 1000], [1,15,225,3375]])
b = np.array([f(1), f(4), f(10), f(15)])
solution = sp.linalg.solve(a,b)
x = np.arange(1, 15, 0.1)
y = solution[0] + x * solution[1] + x**2* solution[2] +  x**3 * solution[3] 
plt.plot(x, y)
plt.show()

# Writing solution into the file
file_obj = open('C:\\Users\\Home\\Downloads\\submission-2.txt', 'w')
string = str(round(solution[0],2)) + ' ' + str(round(solution[1],2))  + ' ' + str(round(solution[2],2)) + ' ' + str(round(solution[3],2))
file_obj.write(string)
file_obj.close()

