# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:14:57 2017

@author: Huntrer
"""
import numpy as np
def func(x):
    # Function: f(x)
    fx = np.log(x) - np.exp(-x)
    return fx
def func1(x):
    # Function: f(x)
    fx = np.log(x) - np.exp(-x)

    # Derivative of function: f'(x)
    d_fx = 1.0/x + np.exp(-x)

#    return np.array([fx, d_fx])
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
from scipy.optimize import root
result = root(func,2)
print(result.x)

from scipy.optimize import fsolve
result =fsolve(func,2)
print(result[0])