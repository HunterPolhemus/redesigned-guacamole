# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:45:08 2017

@author: Huntrer
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
import time  # Imports system time module to time your script

plt.close('all')  # close all open figures

def f1simple(x):
    # gamma(2,3) density
    if (x < 0):
        return (0)
    if (x == 0):
        return (np.nan)
    y = np.exp(-2*x)
    return (4 * x**2 * y)
def f1(x):
    # gamma(2,3) density
    if (x < 0):
        return np.array([0, 0, 0])
    if (x == 0):
        return np.array([0, 0, np.nan])
    y = np.exp(-2.0*x)
    return np.array([4.0 * x**2.0 * y, \
      8.0 * x*(1.0-x)*y, \
      8.0*(1 - 4*x + 2 * x**2)*y])
xmin = 0.0
xmax = 6.0
xv = np.arange(xmin, xmax, (xmax - xmin)/200.0)
fx = np.zeros(len(xv),float) # define column vector
for i in range(len(xv)):
    fx[i] = f1(xv[i])[0]

print("fx[0:10]= ", fx[0:10])

fig, ax = plt.subplots()
ax.plot(xv, fx)
ax.plot(xv, np.zeros(len(xv)))
plt.show()