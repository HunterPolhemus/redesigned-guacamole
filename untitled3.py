# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:18:22 2017

@author: Huntrer
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------- 
# Question 1 - part 1
# ----------------------------------------------------------------------------- 
def func(x):
   # Function: f(x) 
   fx = np.log(x) - np.exp(-x)
   return fx

#define the same function but return the derivative
def func1(x):
   # Function: f(x)
   fx = np.log(x) - np.exp(-x)
   # Derivative of function: f'(x)
   d_fx = 1.0/x + np.exp(-x)
   return np.array([fx, d_fx])

#Plot the function
xmin = 1
xmax = 3
xv  = np.linspace(xmin, xmax, 200)
fxv = np.zeros(len(xv),float) #define column vector
for i in range(len(xv)):
   fxv[i] = func(xv[i])

fig, ax = plt.subplots()
ax.plot(xv, fxv)
ax.plot(xv, np.zeros(len(xv)))
# Create a title with a red, bold/italic font
plt.show()

def newtonraphson(ftn, x0, tol = 1e-9, maxiter = 100):
   x = x0
   #x0 is the starting value 
   fx = ftn(x)
   #an array of values consisting of f(x) and f'(x)
   jiter =  0

   # continue iterating until stopping conditions are met
   while ((abs(fx[0]) > tol) and (jiter < maxiter)):
       x = x - fx[0]/fx[1]
       fx = ftn(x)
       jiter =  jiter + 1
       print("At iteration: {} the value of x is {}:" \
         .format(jiter, x))

   # Output depends on success of algorithm
   if (abs(fx[0]) > tol):
       print("Algorithm failed to converge")
       return None
   else:
       print("fx = ", fx[0])
       print("Algorithm converged")
       return x
   
myRoot = newtonraphson(func1, 2)
# 3 is the starting value 
print('--------------------------------')
print('My Root is at {:8.4f}'.format(myRoot))
print('--------------------------------')

def bisection(ftn, xl, xr, tol = 1e-9):
   # applies the bisection algorithm to find x
   # such that ftn(x) == 0
   # we assume that ftn is a function of a single variable
   #
   # x.l and x.r must bracket the fixed point, that is
   # x.l < x.r and ftn(x.l) * ftn(x.r) < 0
   #
   # the algorithm iteratively refines
   # x.l and x.r and terminates when
   # x.r - x.l <= tol

   # check inputs
   if (xl >= xr):
       print("error: xl >= xr")
       return None

   fl = ftn(xl)
   fr = ftn(xr)

   if (fl == 0):
       return xl
   elif (fr == 0):
       return xr
   elif (fl * fr > 0):