# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 05:02:11 2017

@author: Huntrer
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats as st
import time  # Imports system time module to time your script

plt.close('all')  # close all open figures
tic = time.time()
np.random.seed(123456789)

# Uniform distributed random numbers
u = np.random.uniform(20,80,(5000,))
N = 50
fig, ax = plt.subplots()
prob, bins, patches = ax.hist(u, bins=N, align='mid' )
ax.set_ylabel('Number of obs')
ax.set_title('Histogram of uniform random variable')
plt.show()