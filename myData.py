# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:19:37 2017

@author: Huntrer
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
import math as m
import seaborn as sns
import time  # Imports system time module to time your script
import numpy as np
from pandas import DataFrame as df
import pandas as pd
from scipy.stats import trim_mean, kurtosis
from scipy.stats.mstats import mode, gmean, hmean
import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')  # close all open figures

# Read in small data from .csv file
# Filepath

# In windows you can also specify the absolute path to your data file
# filepath =
#question1
filepath ='C:/Users/Huntrer/Downloads/'

df = pd.read_csv(filepath + 'BaltimoreData.csv')

print(res.summary2())

#question2
print(df)
# Summary stats
print(df.describe())
print("Summary Stats")
print("-------------")
Populations = df['Population'].values
N = len(Populations) # number of obs.
print(st.describe(Populations))

Medianincomev = df['Median Income'].values
N = len(Medianincomev) # number of obs.
print(st.describe(Medianincomev))


Unemployedv = df['Unemployed'].values
N = len(Unemployedv) # number of obs.
print(st.describe(Unemployedv))

Families_in_Poverty = df['Families in Poverty'].values
N = len(Families_in_Poverty) # number of obs.
print(st.describe(Families_in_Poverty))

Bachelors_degree = df['Bachelors degree'].values
N = len(Bachelors_degree) # number of obs.
print(st.describe(Bachelors_degree))

Juvenile_Arrest_Rate = df['Juvenile Arrest Rate'].values
N = len(Juvenile_Arrest_Rate) # number of obs.
print(st.describe(Juvenile_Arrest_Rate))

Homicide_Incidence_Rate = df['Homicide Incidence Rate'].values
N = len(Homicide_Incidence_Rate) # number of obs.
print(st.describe(Homicide_Incidence_Rate))

Life_Expectancy = df['Life Expectancy'].values
N = len(Life_Expectancy) # number of obs.
print(st.describe(Life_Expectancy))

Top_causes_of_death = df['Top causes of death'].values
N = len(Top_causes_of_death) # number of obs.
print(st.describe(Top_causes_of_death))

#question3



nans = df.shape[0] - df.dropna().shape[0]

print('{} rows have missing values'.format(nans))
print(df[df.isnull().any(axis=1)])
df.fillna(value=0, inplace=True)
print(df)


xv= df['Population'].values
yv = df['Bachelors degree'].values


p = np.polyfit(xv, yv, 1)
print("p = {}".format(p))

# Scatterplot
fig, ax = plt.subplots()
ax.set_title('Linear regression with polyfit()')
ax.plot(xv, yv, 'o', label = 'data')
ax.plot(xv, np.polyval(p,xv),'-', label = 'Linear regression')
ax.legend(['Data', 'OLS'], loc='best')
plt.show()

#question4

# Import the correct version of statsmodels
import statsmodels.api as sm
from patsy import dmatrices
# Run  regression

y, X = dmatrices('y ~ x', data=df, return_type='dataframe')
res = sm.OLS(y, X).fit()

y, X = dmatrices('Juvenile_Arrest_Rate ~ Populations + Medianincomev + Unemployedv + Families_in_Poverty + Bachelors_degree', data=df, return_type='dataframe')

# Define the model
logit = sm.Logit(y, X)

# fit the model
res = logit.fit()

# Print results
print(res.summary())

#question5
#make dummy variable
dummies = pd.get_dummies(df['small_counties'], prefix = 'S')
    for Population < 6500
dummies = pd.get_dummies(df['middle_counties'], prefix = 'M')
    for Population in range(6500,10000)
dummies = pd.get_dummies(df['large_counties'], prefix = 'L')
    for Population > 10000
df = df.join(dummies)
print(df.head())



# Import the correct version of statsmodels
import statsmodels.api as sm
from patsy import dmatrices
# Run  regression

y, X = dmatrices('y ~ x', data=df, return_type='dataframe')
res = sm.OLS(y, X).fit()

y, X = dmatrices('Juvenile_Arrest_Rate ~ small_counties + middle_counties + large_counties + Medianincomev + Unemployedv + Families_in_Poverty + Bachelors_degree', data=df, return_type='dataframe')

# Define the model
logit = sm.Logit(y, X)

# fit the model
res = logit.fit()

# Print results
print(res.summary())