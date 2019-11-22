# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:15:25 2017

@author: Huntrer
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:53:45 2017

@author: Kaitlyn
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
import math as m
import seaborn as sns
import time  # Imports system time module to time your script
import statsmodels.api as sm
from patsy import dmatrices

# Read in small data from .csv file
# Filepath
filepath = 'C:/Users/Huntrer/Downloads/'


# ------------- Load data --------------------
df = pd.read_csv(filepath + 'data431.csv',
dtype={'Frequency': float})
df = df.rename(columns=lambda x: x.strip())
# Make new column with CPI adjusted 
df['RealTuitionFees_IS'] = (df['TuitionFees_IS']/df['CPI'])* (224.94)
df['RealTuitionFees_OS'] = (df['TuitionFees_OS']/df['CPI'])* (224.94)
df['RealFunding'] = (df['FundingInMillions']/df['CPI'])* (224.94)
#when describing summary statistics we used CPI to adjust for inflation and all monies are expressed in 2011 dollars 

df1 = df.groupby(['Year'])['RealTuitionFees_IS'].mean()
df2 = df.groupby(['Year'])['RealTuitionFees_OS'].mean()
df3 = df.groupby(['Year'])['AA_Enroll_YearOne'].mean()
df4 = df.groupby(['Year'])['AA_Grad_FourYr'].mean()
df5 = df.groupby(['Year'])['White_Enroll_YearOne'].mean()
df6 = df.groupby(['Year'])['White_Grad_FourYr'].mean()
df7 = df.groupby(['Year'])['RealFunding'].mean()
df8 = df.groupby(['Year'])['TotalStudents'].mean()

#PLOT FOR IN STATE TUITION OVER TIME
fig, ax = plt.subplots()
ax.set_title('Average In State Tuition Over Time')
xv = np.linspace(1994,2011, 18)
yv = df1.values
ax.set_xlabel('Year')
ax.set_ylabel('Tuition in Dollars')
ax.plot(xv, yv, label = 'data')
plt.show()

#PLOT FOR OUT OF STATE TUITION OVER TIME
fig, ax = plt.subplots()
ax.set_title('Average Out of State Tuition Over Time')
xv = np.linspace(1994,2011, 18)
yv = df2.values
ax.set_xlabel('Year')
ax.set_ylabel('Tuition in Dollars')
ax.plot(xv, yv, label = 'data')
plt.show()

#PLOT FOR INITIAL AFRICAN AMERICAN ENROLLMENT OVER TIME
fig, ax = plt.subplots()
ax.set_title('Initial African American Enrollment Over Time')
xv = np.linspace(1994,2011, 18)
yv = df3.values
ax.set_xlabel('Year')
ax.set_ylabel('%')
ax.plot(xv, yv, label = 'data')
plt.show()

#PLOT FOR INITIAL WHITE ENROLLMENT OVER TIME
fig, ax = plt.subplots()
ax.set_title('Initial White Enrollment Over Time')
xv = np.linspace(1994,2011, 18)
yv = df5.values
ax.set_xlabel('Year')
ax.set_ylabel('%')
ax.plot(xv, yv, label = 'data')
plt.show()

#PLOT FOR AFRICAN AMERICAN GRADUATION WITHIN 4 YEARS
fig, ax = plt.subplots()
ax.set_title('African American Graduation Within Four Years')
xv = np.linspace(1994,2011, 18)
yv = df4.values
ax.set_xlabel('Year')
ax.set_ylabel('%')
ax.plot(xv, yv, label = 'data')
plt.show()

#PLOT FOR AFRICAN AMERICAN GRADUATION WITHIN 4 YEARS
fig, ax = plt.subplots()
ax.set_title('White Graduation Within Four Years')
xv = np.linspace(1994,2011, 18)
yv = df6.values
ax.set_xlabel('Year')
ax.set_ylabel('%')
ax.plot(xv, yv, label = 'data')
plt.show()

#PLOT FOR TOTAL UNDERGRADUATE ENROLLMENT OVER TIME
fig, ax = plt.subplots()
ax.set_title('Total Undergraduate Enrollment Over Time')
xv = np.linspace(1994,2011, 18)
yv = df8.values
ax.set_xlabel('Year')
ax.set_ylabel('%')
ax.plot(xv, yv, label = 'data')
plt.show()


#REGRESSIONS
print("------------------------------")
print("Enrollment, First Year, African American Students")
y, X = dmatrices('AA_Enroll_YearOne ~ TotalStudents + PartTime + FullTime + RealTuitionFees_IS + RealTuitionFees_OS + RealFunding', data=df, return_type='dataframe')
res = sm.OLS(y, X).fit()
# Show coefficient estimates
print(res.summary())
print(res.params)
print("------------------------------")


print("------------------------------")
print("Enrollment, First Year, White Students")
y, X = dmatrices('White_Enroll_YearOne ~ TotalStudents + PartTime + FullTime + RealTuitionFees_IS + RealTuitionFees_OS + RealFunding', data=df, return_type='dataframe')
res = sm.OLS(y, X).fit()
# Show coefficient estimates
print(res.summary())
print(res.params)
print("------------------------------")


print("------------------------------")
print("Graduaton Rate, Four Years, African American Students")
y, X = dmatrices('AA_Grad_FourYr ~ TotalStudents + PartTime + FullTime + RealTuitionFees_IS + RealTuitionFees_OS + RealFunding', data=df, return_type='dataframe')
res = sm.OLS(y, X).fit()
# Show coefficient estimates
print(res.summary())
print(res.params)
print("------------------------------")


print("------------------------------")
print("Graduaton Rate, Four Years, White Students")
y, X = dmatrices('White_Grad_FourYr ~ TotalStudents + PartTime + FullTime + RealTuitionFees_IS + RealTuitionFees_OS + RealFunding', data=df, return_type='dataframe')
res = sm.OLS(y, X).fit()
# Show coefficient estimates
print(res.summary())
print(res.params)
print("------------------------------")



print("------------------------------")
print("All Students")
y, X = dmatrices('TotalStudents ~ PartTime + FullTime + RealTuitionFees_IS + RealTuitionFees_OS + RealFunding', data=df, return_type='dataframe')
res = sm.OLS(y, X).fit()
# Show coefficient estimates
print(res.summary())
print(res.params)
print("------------------------------")

#SUMMARY STATS
print(df.describe())
