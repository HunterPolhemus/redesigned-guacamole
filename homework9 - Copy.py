# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:18:17 2017

@author: Huntrer
"""

'methodPython'
import numpy as np
import matplotlib.pyplot as plt
#
import time  # Imports system time module to time your script
#

print('----------------question1----------')
plt.close('all')  # close all open figures
##part1
#def func(x):
#    # Function: f(x)
#    fx = np.log(x) - np.exp(-x)
#    return fx
#def func1(x):
#     Function: f(x)
#     fx = np.log(x) - np.exp(-x)
#
#    # Derivative of function: f'(x)
#    d_fx = 1.0/x + np.exp(-x)
#
#    return np.array([fx, d_fx])
#part2
#def bisection(ftn, xl, xr, tol = 1e-9):
#    # applies the bisection algorithm to find x
#    # such that ftn(x) == 0
#    # we assume that ftn is a function of a single variable
#    #
#    # x.l and x.r must bracket the fixed point, that is
#    # x.l < x.r and ftn(x.l) * ftn(x.r) < 0
#    #
#    # the algorithm iteratively refines
#    # x.l and x.r and terminates when
#    # x.r - x.l <= tol
#
#    # check inputs
#    if (xl >= xr):
#        print("error: xl >= xr")
#        return None
#
#    fl = ftn(xl)
#    fr = ftn(xr)
#
#    if (fl == 0):
#        return xl
#    elif (fr == 0):
#        return xr
#    elif (fl * fr > 0):
#        xm = (xl + xr)/2.0
#        xw= xl-xr
#        xl=xm-xw
#        xr=xm+xw
##        return xl
#
#    # successively refine x.l and x.r
#    n = 0
#    while ((xr - xl) > tol):
#        xm = (xl + xr)/2.0
#        fm = ftn(xm)
#        if (fm == 0):
#            return fm
#        elif (fl * fm < 0):
#            xr = xm
#            fr = fm
#        else:
#            xl = xm
#            fl = fm
#        n = n + 1
#        print("at iteration: {} the root lies between {} and {}" \
#            .format(n, xl, xr))
#    # return (approximate) root
#    return (xl + xr)/2.0
#        
#
#myRoot = bisection(func,1,2)

#
#    return np.array([fx, d_fx])
#part3
#def func(x):
#    # Function: f(x)
#    fx = (x**3)-(7*x**2)+(14*x)-(8)
#    return fx
#def func1(x):
#    # Function: f(x)
#    fx = (x**3)-(7*x**2)+(14*x)-(8)
#
#    # Derivative of function: f'(x)
#    d_fx = (3*x**2)-(14*x)+(14)-(8)
#    return np.array([fx, d_fx])
#part4
#define the same function but return the derivative
#def func1(x):
#   # Function: f(x)
#   fx = (np.log(x))*(np.exp(-x))
#   # Derivative of function: f'(x)
#   d_fx = 1.0/x*(np.exp(-x)) + (-np.exp(-x))*(np.log(x))
#   return np.array([fx, d_fx])
#
#def newtonraphson(ftn, x0, tol = 1e-9, maxiter = 100):
#   x = x0
#   #x0 is the starting value 
#   fx = ftn(x)
#   #an array of values consisting of f(x) and f'(x)
#   jiter =  0
#
#   # continue iterating until stopping conditions are met
#   while ((abs(fx[0]) > tol) and (jiter < maxiter)):
#       x = x - fx[0]/fx[1]
#       fx = ftn(x)
#       jiter =  jiter + 1
#       print("At iteration: {} the value of x is {}:" \
#         .format(jiter, x))
#
#   # Output depends on success of algorithm
#   if (abs(fx[0]) > tol):
#       print("Algorithm failed to converge")
#       return None
#   else:
#       print("fx = ", fx[0])
#       print("Algorithm converged")
#       return x
#   
#myRoot = newtonraphson(func1, 2)
#print('--------------------------------')
#print('My Root is at {:8.4f}'.format(myRoot))
#print('--------------------------------')
#def newtonraphson(ftn, x0, tol = 1e-9, maxiter = 100):
#    # Newton_Raphson algorithm for solving ftn(x)[1] == 0
#    # we assume that ftn is a function of a single
#    # variable that returns the function value and
#    # the first derivative as a vector of length 2
#    #
#    # x0 is the initial guess at the root
#    # the algorithm terminates when the function
#    # value is within distance tol of 0, or the
#    # number of iterations exceeds maxiter
#
#    x = x0
#    fx = ftn(x)
#    jiter =  0
#
#    # continue iterating until stopping conditions are met
#    while ((abs(fx[0]) > tol) and (jiter < maxiter)):
#        x = x - fx[0]/fx[1]
#        fx = ftn(x)
#        jiter =  jiter + 1
#        print("At iteration: {} the value of x is {}:" \
#          .format(jiter, x))
#
#    # Output depends on success of algorithm
#    if (abs(fx[0]) > tol):
#        print("Algorithm failed to converge")
#        return None
#    else:
#        print("fx = ", fx[0])
#        print("Algorithm converged")
#        return x
#    
#        if (xl >= xr):
#        print("error: xl >= xr")
#        return None
##this is used in part 2
#    fl = ftn(xl)
#    fr = ftn(xr)
#
#    if (fl == 0):
#        return xl
#    elif (fr == 0):
#        return xr
#    elif (fl * fr > 0):
#        xm = (xl + xr)/2.0
#        xw= xl-xr
#        xl=xm-xw
#        xr=xm+xw
#myRoot = newtonraphson(func1, 2) #was used for part1 
#myRoot = newtonraphson(func1, 0) # was used for part2
#this was used for part 3
#myRoot = newtonraphson(func1, 1.1,1.2,1.3,)
#myRoot = newtonraphson(func1, 1.4,1.5,1.6,)
#myRoot = newtonraphson(func1, 1.7,1.8,1.9)
#used in part 4
#myRoot = newtonraphson(func1, 2)


#print('--------------------------------')
#print('My Root is at {:8.4f}'.format(myRoot))
#print('--------------------------------')



print('----------------question2----------')

def func(x):
   # Function: f(x) 
   fx = ((x - 1)**3) - (2*x**2) + 10 - (np.sin(x))
   return fx

#define the same function but return the derivative
def func1(x):
   # Function: f(x)
   fx = ((x - 1)**3) - (2*x**2) + 10 - (np.sin(x))
   # Derivative of function: f'(x)
   d_fx = d_fx = (3*((x-1)**2)) - (4*x) - (np.cos(x))
   return np.array([fx, d_fx])

def bisection(ftn, xl, xr, tol = 1e-9):

   # check inputs
   if (xl >= xr):
       print("error: xl >= xr")
       return None

   fl = ftn(xl)
   fr = ftn(xr)
       elif (fl * fm < 0):
           xr = ((xl + xr)/2.0) + (xr - xl)
           fr = fm
       else:
           xl = ((xl + xr)/2.0) - (xr - xl)
           fl = fm
       print("error: ftn(xl) * ftn(xr) > 0")
       return None

   # successively refine x.l and x.r
   n = 4
   while ((xr - xl) > tol):
       xm = (xl + xr)/2.0
       fm = ftn(xm)
       if (fm == 0):
           return fm
       elif (fl * fm < 0):
           xr = ((xl + xr)/2.0) + (xr - xl)
           fr = fm
       else:
           xl = ((xl + xr)/2.0) - (xr - xl)
           fl = fm
       n = n + 1
       print("at iteration: {} the root lies between {} and {}" \
           .format(n, xl, xr))
   # return (approximate) root
   return (xl + xr)/2.0

myRoot = bisection(func, 1,2)

print("--------------------------------")
print('My root is at {:8.4f}'.format(myRoot))
print("--------------------------------")

#     return np.array([fx, d_fx])
#def bisection(ftn, xl, xr, tol = 1e-9):
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
#    if (xl >= xr):
#        print("error: xl >= xr")
#        return None
#
#    fl = ftn(xl)
#    fr = ftn(xr)
#
#    if (fl == 0):
#        return xl
#    elif (fr == 0):
#        return xr
#    elif (fl * fr > 0):
#        print("error: ftn(xl) * ftn(xr) > 0")
#        return None
#
#    # successively refine x.l and x.r
#    n = 0
#    while ((xr - xl) > tol):
#        xm = (xl + xr)/2.0
#        fm = ftn(xm)
#        if (fm == 0):
#            return fm
#        elif (fl * fm < 0):
#            xr = xm
#            fr = fm
#        else:
#            xl = xm
#            fl = fm
#        n = n + 1
#        print("at iteration: {} the root lies between {} and {}" \
#            .format(n, xl, xr))
#    # return (approximate) root
#    return (xl + xr)/2.0


#myRoot = bisection(func, 1,2)
#
#print('--------------------------------')
#print('My Root is at {:8.4f}'.format(myRoot))
#print('--------------------------------')