#!/usr/bin/env python
# coding: utf-8

# # Install and Import Packages

# In[1]:


# install this package 
get_ipython().system('pip install pandas-datareader')


# In[2]:


# import packages
import pandas as pd
import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Gather Data From Yahoo Finanace

# In[3]:


# Setting dates of data pull
startdate = '2017-01-01'
enddate = '2020-12-31'

# Apply Pandas DataReader
AMD = pdr.DataReader('AMD','yahoo', startdate, enddate)
AAPL = pdr.DataReader('AAPL','yahoo', startdate, enddate)
MSFT = pdr.DataReader('MSFT','yahoo', startdate, enddate)
ORCL = pdr.DataReader('ORCL','yahoo', startdate, enddate)


# In[4]:


AMD.head()


# In[5]:


AMD.tail()


# In[6]:


AAPL.tail()


# In[7]:


MSFT.tail()


# In[8]:


ORCL.tail()


# # Create a Portfolio of Selected Stocks

# In[9]:


# Normalizing stock prices (cumulative return)
for stock in (AMD, AAPL, MSFT, ORCL):
    stock['Normalizing Return'] = stock['Adj Close']/stock.iloc[0]['Adj Close']


# In[10]:


# Example of ORCL from the for loop
stock.head()


# In[11]:


AAPL.head()


# In[12]:


# Setting weights
for stock, allo in zip((AMD, AAPL, MSFT, ORCL), [0.25, 0.25, 0.25, 0.25]):
    stock['Allocation'] = stock['Normalizing Return']*allo


# In[13]:


# Examining the allocation of a stock
MSFT.head()


# In[14]:


# Assigning a value of $10,000 to the portfolio
for stock in (AMD, AAPL, MSFT, ORCL):
    stock['Position Value'] = stock['Allocation']*10000


# In[15]:


# Examining the amount in AMD
AMD.head()


# # Setting Up Portfolio Dollar Values

# In[16]:


# Create a list of all position values
position_values = [AMD['Position Value'], AAPL['Position Value'], MSFT['Position Value'], ORCL['Position Value']]

# Concatenate the list of position values
position_values = pd.concat(position_values, axis=1)

# Name columns
position_values. columns = ['AMD','AAPL','MSFT','ORCL']

# Add a total for entire portfolio
position_values['Total'] = position_values.sum(axis=1)
position_values.head()


# In[17]:


# Plot total portfolio
position_values['Total'].plot(figsize=(12,8), title='$10k Portfolio')


# In[18]:


# Plotting each stock within portfolio
position_values.drop('Total', axis=1).plot(figsize=(12,8), title='Individual Stocks From Portfolio')


# In[19]:


# Cumulative portfolio return in terms of percent
cumulative_return = (position_values['Total'][-1]/position_values['Total'][0]-1) * 100
cumulative_return


# # Daily Returns

# In[20]:


# Calculating daily returns
position_values['Daily Return'] = position_values['Total'].pct_change(1)
position_values.head()


# In[21]:


# Average daily return
position_values['Daily Return'].mean()


# In[22]:


# Standard deviation
position_values['Daily Return'].std()


# In[23]:


# Sharpe ratio (assuming Risk Free Rate to be close to zero)
sharpe_ratio = position_values['Daily Return'].mean() / position_values['Daily Return'].std()
sharpe_ratio


# In[24]:


# Annualize Sharpe ratio
sharpe_ratio_annualized = (252**0.5) * sharpe_ratio
sharpe_ratio_annualized


# # Set Up for Portfolio Optimization

# In[25]:


# concatenate stocks and rename columns
stocks = pd.concat([AMD['Adj Close'], AAPL['Adj Close'], MSFT['Adj Close'], ORCL['Adj Close']], axis=1)
stocks.columns = ['AMD','AAPL','MSFT','ORCL']
stocks.head()


# In[26]:


# Converting to percent change
stock_return = stocks.pct_change(1)
stock_return.head()


# # Prepare variables for Portfolio Optimization

# In[27]:


# Setting up for 10k different portfolio weighting combinations
number_ports = 10000
all_weights = np.zeros((number_ports, len(stocks.columns)))
all_weights


# In[28]:


# Preallocating space for portfolio calculations
returns_array = np.zeros(number_ports)
volatility_array = np.zeros(number_ports)
sharpe_array = np.zeros(number_ports)


# # Calculate Portfolio Combinations

# In[29]:


# For replication from randomizer
import random
random.seed(3)
# Fun fact, different randomizer for numpy
np.random.seed(3)

for index in range(number_ports):
    #generate random weights
    numbers = np.array(np.random.random(4))
    weights = numbers/np.sum(numbers)
    
    #save weights
    all_weights[index, :] = weights
    
    #expected return
    returns_array[index] = np.sum(stock_return.mean() * 252 * weights)
    
    #expected volatility = square root(Weights-Transposed * Covariance Matrix * Weights)
    volatility_array[index] = np.sqrt(np.dot(weights.T, np.dot(stock_return.cov() * 252, weights)))
    
    #Sharpe ratio
    sharpe_array[index] = returns_array[index] / volatility_array[index]


# In[30]:


#Print all weight combinations
print("All Weights:", all_weights)

#Print first weights
print("First combination:", all_weights[0])


# In[33]:


#Print all Sharpe ratios
print("All Sharpe Ratios:", sharpe_array)

#Print first Sharpe ratio
print("Sharpe ratio of first portfolio:", sharpe_array[0])


# # Portfolio Weights of Highest Sharpe Ratio

# In[34]:


#Find highest Sharpe ratio
sharpe_array.max()


# In[36]:


#Find by index
index_max_sharpe = sharpe_array.argmax()
index_max_sharpe


# In[37]:


#Taking weights of the best portfolio
print(all_weights[index_max_sharpe, :])
print(stocks.columns)


# # Plot Efficient Frontier

# In[39]:


# plot heatmap
plt.figure(figsize=(12,8))
plt.scatter(volatility_array, returns_array, c=sharpe_array, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')


# In[40]:


#Plot optimal portfolio
max_sharpe_return = returns_array[index_max_sharpe]
max_sharpe_volatility = volatility_array[index_max_sharpe]

# Plot heatmap
plt.figure(figsize=(12,8))
plt.scatter(volatility_array, returns_array, c=sharpe_array, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

# Add orange dot for easy viewing
plt.scatter(max_sharpe_volatility, max_sharpe_return, c='orange', edgecolors='black')


# In[ ]:




