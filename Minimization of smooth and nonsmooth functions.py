
# coding: utf-8

# Minimization of a smooth function
import numpy as np
import scipy as sp
import matplotlib as mp
import math
from matplotlib import pylab as plt
from scipy import optimize

# Defining Functions
def f(x):
    f = math.sin(x[0]/5.0)*math.exp(x[0]/10.0)+5*math.exp(-x[0]/2.0)
    return f

# Finding the minimum using the standard parameters in the function scipy.optimize.minimize
print optimize.minimize(f,[1,30] )

# The search for a minimum using the BFGS method, the initial approximation point 2
print optimize.minimize(f, [2, 2], method='BFGS')

# The search for a minimum using the BFGS method, the initial approximation point 30
print optimize.minimize(f, [30, 30], method='BFGS')

# Methods of global optimization
print optimize.differential_evolution(f, [(1, 30)])

# Minimization of a nonsmooth function

# Defining Functions and drawing plot
def h1(x):
    h1 = int(f1(x))
    return h1
def f1(x):
    f1 = math.sin(x/5.0)*math.exp(x/10.0)+5*math.exp(-x/2.0)
    return f1
x = np.arange(1,30,1)
y = [h1(i) for i in x]
plt.plot(x, y)
plt.show()

# The search for a minimum using the BFGS method, the initial approximation point 30
def h(x):
    h = int(f(x))
    return h
print optimize.minimize(h, [30, 30], method='BFGS')

# Methods of global optimization
print optimize.differential_evolution(h, [(1, 30)])

