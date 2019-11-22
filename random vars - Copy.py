# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:44:16 2017

@author: Huntrer
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats as st
import time  # Imports system time module to time your script
#
##np.random.seed(4325554)
##myNumber = np.random.uniform(0,1)
##print('My 1. random number in [0,1] is {}'.format(myNumber))
##
##
##myNumber = np.random.uniform(0,1)
##print('My 2. random number in [0,1] is {}'.format(myNumber))
##
##myNumber = np.random.uniform(0,1)
##print('My 3. random number in [0,1] is {}'.format(myNumber))
##
##uv = np.random.uniform(0,1,(10000,))
##u = np.random.uniform(0,1,(10000,))
##N = 50
##fig, ax = plt.subplots()
##prob, bins, patches = ax.hist(u, bins=N, align='mid' )
##ax.set_ylabel('Number of obs')
##ax.set_title('Histogram of uniform random variable')
#
#
#
## Draws 10,000 standard normally distributed random numbers
#z = np.random.normal(0,1,(10000,))
#zv = np.random.normal(10,5,(10000,))
#
#
#N = 50
#fig, ax = plt.subplots()
#prob, bins, patches = ax.hist(z, bins=N, align='mid' )
#ax.set_ylabel('Number of obs')
#ax.set_title('Histogram of normal random variable')
#
#counter = 0
#for z in zv:
#    if (zv[i] > 10) and (zv[i]<15):
#        counter = counter + 1
#        
#        
#myFrac = counter/1000*100
#print('Fraction of numbers within one st.dev. of mean is: {}'.format(counter/1000*100))
#
#
#z1 = np.random.normal(0,1,(10000,))
#z2 = np.random.normal(0,2,(10000,))
#
#fig, ax = plt.subplots(2,1)
##
#prob, bins, patches = ax[0].hist(z1, bins=N, align='mid' )
#ax[0].set_ylabel('Number of obs')
#ax[0].set_title('Histogram of N(0,1) random variable')
#ax[0].set_xlim([-10, 10])
##
#prob, bins, patches = ax[1].hist(z2, bins=N, align='mid' )
#ax[1].set_ylabel('Number of obs')
#ax[1].set_title('Histogram of N(0,2) random variable')
#ax[1].set_xlim([-10, 10])
##
#plt.show()
#dof = 29
#xv = np.random.standard_t(dof, 5)
#print(xv)
#
#
#def student_tvariate(df): # df is the number of degrees of freedom
#    if df < 2 or int(df) != df:
#        raise ValueError('student_tvariate: df must be a integer > 1')
#    x = np.random.normal(0, 1)
#    y = np.random.gamma(df/2.0, 2)
#    return x / (np.sqrt(y/df))
#
#t = np.zeros((10000),float)
#for i in range(10000):
#    t[i] = student_tvariate(20)
#    
#    
#    fig, ax = plt.subplots()
##
#prob, bins, patches = ax.hist(t, bins=N, align='mid' )
#ax.set_ylabel('Number of obs')
#ax.set_title('Histogram of T(dof=20) random variable')
##
#plt.show()
#slow solution
#integerList = np.random.randint(1, 5, 10)
#print(integerList)
#integerList = np.random.randint(7, 11, 5)
#print(integerList)
#
#
#integerList = np.random.randint(7, 11, 10000)
#counter7 = 0
#counter8 = 0
#counter9 = 0
#counter10 = 0
#for val in integerList:
#    if val == 7:
#        counter7 = counter7 +1
#        
#    if val == 8:
#        counter8 = counter8 +1
#        
#    if val == 9:
#        counter9 = counter9 +1
#       
#    if val == 10:
#        counter10 = counter10 +1
#        
#print('we  got {} times the value of 7'.format(counter7))
#print('we  got {} times the value of 7'.format(counter8))
#print('we  got {} times the value of 7'.format(counter9))
#print('we  got {} times the value of 7'.format(counter10))
#xv = np.bincount(integerList)
#print(xv)
#
#simple solution
#fig, ax = plt.subplots()
#ax.bar(7 + np.arange(4), xv[7:11], align='center')
#ax.set_xticks(7. + np.arange(4))
#ax.set_ylabel('Number of obs')
#ax.set_title('Bar Chart of Random Number Occurrences')
#plt.show()

# Set random seed
np.random.seed(123456789)
class RandomMan(object):
    """This is a random man object.
    RandomMan has a name, numer of children and income.
    RandomMan can showMan(), earnIncome(),
    buyInsurance() and experience and incomeShock()"""
    def __init__(self, name = 'John Doe'):
        """Initialize the man-object with a
        random nr. of children between 0 and 10 and
        with random income drawn from a normal distribution
        and an insurance state of 0."""
        self.name = name
        self.children = np.random.randint(0, 10, 1)
        self.income = np.random.normal(50000, 16000, 1)
        self.insurance = 0  # 0 no insurance, 1 has insurance
    def showMan(self):
        """Method: showMan() prints out
        the variables stored in the man
        object."""
        print("\n")
        print("Hello, let me introduce myself.")
        print("-------------------------------")
        print("My name is {}".format(self.name))
        if self.children == 1:
            # Get grammar right child/children
            print("I have {:1.0f} child" \
                .format(np.asscalar(self.children)))
        else:
            print("I have {:1.0f} children" \
                .format(np.asscalar(self.children)))
        print("My income is ${:6.0f}"\
          .format(np.asscalar(self.income)))
        if self.insurance == 0:
            print("I have NO insurance")
        else:
            print("I have insurance")
    def earnIncome(self, workTime = 0.0):
        """Make man richer by working."""
        self.income += np.sqrt(1 + workTime)
    def buyInsurance(self):
        """Buy insurance if the man is lucky.
        Lucky is define as a [0, 1] random number
        to be smaller than 0.4. So the guy has
        a 40% chance of being lucky. If she is lucky
        she will buy insurance."""
        if np.random.rand()<0.4:
            # Insurance state flips to 1
            self.insurance = 1
            # Insurance costs $100, so the premium is subtracted
            # from her income
            self.income += -100
        else:
            # Insurance state flips to 0
            self.insurance = 0

    def shockIncome(self):
        """Shocks income randomly with a negative
        value between -5000 and 0."""
        if self.insurance == 0:
            # If she has no insurance, her income
            # is randomly reduced
            self.income += np.random.uniform(-5000, 0, 1)
            randomManList = []
randomManList = []
print(' --- Create men --- ')
for i in range(10):
    # Here we create the randomMan objects and store them in
    # the list
    randomManList.append(RandomMan())
    randomManList[i].showMan()