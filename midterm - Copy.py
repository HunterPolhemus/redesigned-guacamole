# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:59:15 2017

@author: Huntrer
"""

import math as m
import numpy as np
import numpy as np
import matplotlib.pyplot as plt


x = [3.2,6,7.8,1,3,2.5,100]
less_than_four = list(filter(lambda x: x < 4,x))


less_than_four = [3.2, 1, 3, 2.5]
plusfive = list(map(lambda x: x+5, less_than_four))
print(plusfive)


x = [3.2,6,7.8,1,3,2.5,100]
for x in range (2,5):
    x = -1
print(x)


"part 3"

np.mean(x)
print(np.mean(x))
sqv=x-(np.mean(x))
print(sqv)

'------------------question2-----'
x=[1.,5.5,7.2,4.2,-2.7,-5.4,8.9]
y=[0.1,1.5,1.8,-4.2,2.7,-9.4,-1.9]


# get the mean of `X` (add all the vals in `X` and divide by
# the length
x_mean = float(sum(X)) / len(X)
print(x_mean)
# mean for `Y`
y_mean = float(sum(Y)) / len(Y)
print(y_mean)

cov = 0


for y_idx,y in enumerate(Y):
    for x_idx,x in enumerate(X):

     
        cov += (x - x_mean) * (y - y_mean) 

print (cov) 

'--------------questions3----------'
xv = np.linspace(-4, 4,)
yv = np.zeros(len(xv))

for i,x in enumerate(xv):
    if x < 0:
        yv[i] = np.abs(x)
        yv[i] = np.log(x)
        
    elif (x >= 0) & (x < 2):
        yv[i] = -x
    
    elif (x >= 0) & (x < 2):
        yv[i] =(x^2)/(3-x)

fig, ax = plt.subplots()
ax.plot(xv, yv, 'b.')
# For x/y axes in red
ax.axvline(x=0, color = 'r')
ax.axhline(y=0, color = 'r')
# For the dotted vertical lines at the jump points
ax.plot((0, 0), (-1,0), 'k:')
ax.plot((1, 1), (-1,1), 'k:')
ax.plot((2, 2), (-1,1), 'k:')
ax.set_title('Composite discontinuous function')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
plt.show()
'------------------question4-----'
A = np.array([[1.2, 3.4, 10.3],[2, 8, 78], [35, -36, 8]])
print(A)
np.fill_diagonal(A, -5)
print(A)
'--------part-b------------'
A = np.array([[1.2, 3.4, 10.3],[2, 8, 78], [35, -36, 8]])
print(A)     
A[1:,0] = 100
A[2:,1] = 100
A[0,1:] = 100
A[1,2:] = 100
print("A = ", A)    
'------------------question5-----'
personlist = [['Julie', 'married', 35000, 'Jack'],['Angie', 'not married', 55000, 'na',],['Sarah', 'married', 45000, 'Jim'],['Jack', 'married', 35000, 'Julie'],['John', 'not married', 25000, 'na'],['Jim', 'married', 35000, 'Sarah']]
marriedlist = [[]]