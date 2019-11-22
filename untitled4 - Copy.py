# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:29:59 2017

@author: Huntrer
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:22:47 2017

@author: Kaitlyn
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats as st
import time


# ----------------------------------------------------------------------------- 
# Question 1 
# ----------------------------------------------------------------------------- 
import random

total_heads = 0
total_tails = 0
count = 0


while count < 100:

    coin = random.randint(1, 2)

    if coin == 1:
        print("Heads!\n")
        total_heads += 1
        count += 1

    elif coin == 2:
        print("Tails!\n")
        total_tails += 1
        count += 1

print("\nOkay, you flipped heads", total_heads, "times ")
print("\nand you flipped tails", total_tails, "times ")


# ----------------------------------------------------------------------------- 
# Question 2
# ----------------------------------------------------------------------------- 
def draw_random_uniform(N):
    import random                      # Use Python's standard random module.
    M, p = 0, 0                        # Assign intitial variable values.
    for e in range(N):                 # Draw N
        r = random.uniform(0, 1)       # random numbers in range [a, b).
        if r > 0.5 and r < 0.6:        # If in interval (0.5, 0.6) then
            M += 1                     # count M and
            p = float(M)/N             # compute probability

    return p 

# Test cases
if __name__ == '__main__':
    print ("""
    Probabilities for drawing a number between 0.5 and 0.6.
    N draws, N=100 N=1000 N=10000
    """)

P = draw_random_uniform(100)
print('The probability when N = 100 is', P)
P = draw_random_uniform(1000)
print('The probability when N = 1000 is', P)
P = draw_random_uniform(10000)
print('The probability when N = 10000 is', P)

# ----------------------------------------------------------------------------- 
# Question 3
# ----------------------------------------------------------------------------- 

import random

rolled = []
rolledtimes = 0;
biggest = []

freq = int(input('How many times would you like to roll the dice?'))

def roll():
    rand = random.randrange(1,7)
    return rand
def probability():
    for i in range(0,6):
        print('Calculation of probability:')
        percentage = "{:.2f}".format((count[i] / freq)*100)
        percent = str(percentage) + '%'
        print(' ', i + 1, ':', percent)
def theoretical():
    result = "{:.2f}".format((1/6)*freq)
    denominator = "{:.2f}".format(((1/6)*freq)*6)
    print('\nIn theory, each dice should roll {} out of {} times'.format(result,denominator))
def findBiggest():
    for i in range(1,7):
        biggest.append(rolled.count(i))
    print('\n', 'The most times a dice is rolled is', max(biggest), 'times')
def findSmallest():
    for i in range(1,7):
        biggest.append(rolled.count(i))
    print('\n', 'The least times a dice is rolled is', min(biggest), 'times')

for i in range(1,freq + 1):
    number = roll()
    rolled.append(number)
    rolledtimes+=1
count = [rolled.count(1),rolled.count(2),rolled.count(3),rolled.count(4),rolled.count(5),rolled.count(6)]
print('After being rolled {} times:\n\n1 is rolled {} times\n2 is rolled {} times\n3 is rolled {} times\n4 is rolled {} times\n5 is rolled {} times\n6 is rolled {} times\n'.format(rolledtimes,count[0],count[1],count[2],count[3],count[4],count[5]))

probability()
findBiggest()
findSmallest()
theoretical()

#press run and then enter 1000 in the python console
#