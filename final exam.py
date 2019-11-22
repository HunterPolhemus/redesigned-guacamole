# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 05:02:34 2017

@author: Huntrer
"""

import math as m
import re
import string
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats as st
import random
print("---question1-----")
myString =  'This_dog_likes_to_bark_and_that_cat_eats_mice .'
for i in range(1, len('This_dog_likes_to_bark_and_that_cat_eats_mice .')):
    print('This_dog_likes_to_bark_and_that_cat_eats_mice .'[:i+1])
myString =  'This_dog_likes_to_bark_and_that_cat_eats_mice .'
mylist = myString.split("_")
print(mylist)
for i in range(0, len(mylist), 10):
    for p in mylist[1::2]: print(p)
myString =  'This_dog_likes_to_bark_and_that_cat_eats_mice .'
mylist = myString.split("_")
print(mylist[0], mylist[-1])
print(mylist[1], mylist[-2])
print(mylist[2], mylist[-3])
print(mylist[3], mylist[-4])
print(mylist[4], mylist[-5])
print("---question2-----")
np.random.seed(123456789)

# Uniform distributed random numbers
xv = np.random.uniform(20,80,(5000,))
N = 50000
fig, a = plt.subplots()
prob, bins, patches = xv.hist(xv, bins=N, align='mid' )
xv.set_ylabel('Number of obs')
xv.set_title('Histogram of uniform random variable')
plt.show()
num = int(input('How many numbers: '))
total_sum = 0

for n in range(5000):
    numbers = float(input('five thousand : '))
    total_sum += numbers

avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)
avg = xbar
num = int(input('How many numbers: '))
total_sum = 0

for n in range(300):
    numbers = float(input('three hundred : '))
    total_sum += numbers

avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)
avg = xbarv
np.histogram(xbarv)
plt.show()
print("---question3-----")

print("---question4-----")
print("\n".join(["Hello"*(i%3==0)+"Bye"*(i%5==0) or str(i) for i in range(1,100)]))

