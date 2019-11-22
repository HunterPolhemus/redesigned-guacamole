
"""
Created on Thu Aug 31 14:43:02 2017

@author: Huntrer
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy import stats as st
import time  # Imports system time module to time your script
import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy import stats as st
import time  # Imports system time module to time your script

plt.close('all')  # close all open figure
A = np.array([[0,1,1],[1,0,1],[1,1,0]])
B = np.array([[0,2,3],[0,5,0],[7,0,0]])
print("part1")
C = np.dot(A,B)
print("C=", C)
print("part2")
D =  A+B
print("D=", D)
print("A=", A)
print("B=", B)
print("C=", C)
print("part3")
A = np.array([[0,1,1],[1,0,1],[1,1,0]])      # column vector
Aprime = A.transpose()   # row vector
print("a= {}".format(A))
print("a'= {}".format(Aprime))
print("-----part4---")
print (A[1:2][0:3])
print("------part5----")
a = A[:,2]
b = B[2:3]
print(a)
print(b)
print(a+b)
print("--------question2---")
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import math as m
e=2.17  #e is Euler's number 
sigma=1 
mu=0
xv = np.linspace(-4,4,100)
yv=1/(sigma*(2*m.pi)**(-.5))*e**(-.5)*((((xv-mu)/sigma))**2)

for rows in range (0):
    for cols in range(100):

            print('xv= {}'.format(xv))
            print('yv= {}'.format(yv))
plt.plot(xv, yv, 'b-', linewidth=2, label='xv vs. yv')
plt.show()
print("--------question3---")
w = np.array([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3])
print (w[:])
print (w[:-2])
print (w[::5])
print (w[2:-2:6])
print("-----question4----")
A = np.identity(3)

print(" --- OUTPUT: --- ")
print("A= \n {}".format(A))
B = np.array([[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
print("B=")
print(B)
c=np.vstack((A,B))
print("c=")
print(c)
print("----question5--")
print (c[:,1])
print (c[:,2])
print("-----question6----")
A = np.array([[2,0,0],[0,3,0],[0,0,4],[6,0,0],[0,7,0],[0,0,8]]) 
print(A)
A = np.array([[2,0,0],[0,3,0],[0,0,4],[6,0,0],[0,7,0],[0,0,8]])
for rows in range(1):
    for cols in range(1):
        for i in range(6):
            for j in range(3):
                        if A[i,j]<1 :
                            print("")
                        else:
                            print(A[i,j])
