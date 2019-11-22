# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 23:04:23 2017

@author: Huntrer
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
import math as m
import seaborn as sns
import time  # Imports system time module to time your script

plt.close('all')  # close all open figures


# In windows you can also specify the absolute path to your data file
# filepath =
filepath ='C:/Users/Huntrer/Downloads/'

# ------------- Load data --------------------
df = pd.read_csv(filepath + 'data431_Sheet1.csv',
dtype={'Frequency': float})

# Let's have a look at it, it's a nested list
print(df)
Bowie = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,])
