#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Initial imports
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# import and Reading whale returns
whale_returns_csv = Path("C:/Users/chefd/OneDrive/Desktop/whalecsv/whale_returns.csv")
whale_returns = pd.read_csv(whale_returns_csv, index_col='Date', infer_datetime_format=True, parse_dates=True)
whale_returns = whale_returns.sort_index()
whale_returns.head()


# In[ ]:





# In[3]:


# Count nulls
whale_returns.isnull().mean()
whale_returns.isnull().sum()


# In[4]:


# Drop nulls
whale_returns = whale_returns.dropna()
whale_returns.isnull().sum()


# In[5]:


# import and Reading algorithmic returns
algo_returns_csv = Path("C:/Users/chefd/OneDrive/Desktop/whalecsv/algo_returns.csv")
algo_returns = pd.read_csv(algo_returns_csv, index_col="Date", infer_datetime_format=True, parse_dates=True)
algo_returns = algo_returns.sort_index()
algo_returns.head()


# In[6]:


# Count nulls
algo_returns.isnull().mean()
algo_returns.isnull().sum()


# In[7]:


# Drop nulls
algo_returns = algo_returns.dropna()
algo_returns.isnull().sum()


# In[8]:


# Reading S&P TSX 60 Closing Prices
sp_tsx_history_csv = Path("C:/Users/chefd/OneDrive/Desktop/whalecsv/sp_tsx_history.csv")
sp_tsx_history = pd.read_csv(sp_tsx_history_csv,index_col="Date",parse_dates=True,infer_datetime_format=True)
sp_tsx_history.head(10)


# In[9]:


# Check Data Types
sp_tsx_history.dtypes


# In[10]:


# Fix Data Types
sp_tsx_history["Close"] = sp_tsx_history["Close"].str.replace("$", "", regex=True)
sp_tsx_history["Close"] = sp_tsx_history["Close"].str.replace(",", "")


# In[11]:


sp_tsx_history.head()


# In[12]:


sp_tsx_history["Close"] = sp_tsx_history["Close"].astype('float')
sp_tsx_history.dtypes


# In[13]:


# Calculate Daily Returns
sp_tsx_returns = sp_tsx_history.pct_change()
sp_tsx_returns.head()


# In[14]:


# Drop nulls
sp_tsx_returns.dropna(inplace=True)
sp_tsx_returns.head()


# In[15]:


# Rename `Close` Column to be specific to this portfolio.
sp_tsx_returns.rename(columns={"Close": "S&P tsx 60"}, inplace=True)
sp_tsx_returns.head()


# In[16]:


# Join Whale Returns, Algorithmic Returns, and the S&P TSX 60 Returns into a single DataFrame with columns for each portfolio's returns.
combined_portfolios = pd.concat([whale_returns, algo_returns, sp_tsx_returns], axis="columns", join="inner")
combined_portfolios.head()


# In[17]:


# Plot daily returns of all portfolios
combined_portfolios.plot(figsize=(30, 15))


# In[18]:


# Calculate cumulative returns of all portfolios
# Plot cumulative returns
calcum_returns = (1 + combined_portfolios).cumprod()
calcum_returns.plot(figsize=(30, 15))


# In[19]:


# Box plot to visually show risk
combined_portfolios.plot.box(figsize=(15, 7.5))


# In[20]:


# Calculate the daily standard deviations of all portfolios
combined_portfolios.std()


# In[21]:


# Calculate  the daily standard deviation of S&P TSX 60
sp_tsx_returns.std()

# Determine which portfolios are riskier than the S&P TSX 60              (Could not figure it out)


# In[22]:


# Calculate the annualized standard deviation (252 trading days)
combined_portfolios.std() * np.sqrt(252)


# In[23]:


# Calculate the rolling standard deviation for all portfolios using a 21-day window
combined_portfolios.rolling(window=21).mean()



# In[24]:


# Plot the rolling standard deviation
combined_portfolios.rolling(window=21).std().plot(figsize=(30, 15))


# In[25]:


# Calculate the correlation
calculated_correlation = combined_portfolios.corr()

# Display de correlation matrix
calculated_correlation.style.background_gradient(cmap='coolwarm')


# In[26]:


# Calculate covariance of a single portfolio
covariance = combined_portfolios["Algo 1"].rolling(window=30).cov(combined_portfolios["S&P tsx 60"])


# In[27]:


# Calculate variance of S&P TSX
variance = combined_portfolios["S&P tsx 60"].rolling(window=30).var()


# In[28]:


# Computing beta
algo_beta = covariance / variance


# In[29]:


# Plot beta trend
algo_beta.plot(figsize=(15, 7.5))


# In[30]:


# Use `ewm` to calculate the rolling window 21 day1/2 life          (Could not figure it out)


# In[31]:


# Annualized Sharpe Ratios
sharpe_ratio = (combined_portfolios.mean() * 252) / (combined_portfolios.std() * np.sqrt(252))



# In[32]:


# Visualize the sharpe ratios as a bar plot
sharpe_ratio.plot(kind="bar")


# In[33]:


# MY PORTFOLIO


# In[36]:


# Reading data from 1st stock
Ac_history_csv = Path("C:/Users/chefd/OneDrive/Desktop/csv/AC_closing_data.csv")
Ac_history = pd.read_csv(Ac_history_csv, index_col='Date', infer_datetime_format=True, parse_dates=True)
Ac_history = Ac_history.sort_index()
# Reading data from 2nd stock
CCL_history_csv = Path("C:/Users/chefd/OneDrive/Desktop/csv/CCL_closing_data.csv")
CCL_history = pd.read_csv(CCL_history_csv, index_col='Date', infer_datetime_format=True, parse_dates=True)
CCL_history = Ac_history.sort_index()
# Reading data from 3rd stock
GSL_history_csv = Path("C:/Users/chefd/OneDrive/Desktop/csv/GSL_closing_data.csv")
GSL_history = pd.read_csv(GSL_history_csv, index_col='Date', infer_datetime_format=True, parse_dates=True)
GSL_history = GSL_history.sort_index()


# In[49]:


# Combine all stocks in a single DataFrame
# Reset Date index
my_portfolio = pd.concat([Ac_history, CCL_history, GSL_history], axis="columns", join="inner")
# Reorganize portfolio data by having a column per symbol
columns = ["AC", "CCL", "GSL"]
my_portfolio.columns = columns
my_portfolio.head()


# In[50]:


# Calculate daily returns
my_daily_returns = my_portfolio.pct_change()
my_daily_returns.head()


# In[51]:


# Drop NAs
my_daily_returns.dropna(inplace=True)
# Display sample data
my_daily_returns.head()


# In[52]:


# Set weights
weights = [1/3, 1/3, 1/3]
# calculate portfolio_returns
my_portfolio_returns = my_daily_returns.dot(weights)
# Display sample data
my_portfolio_returns.head(10)


# In[53]:


# Join your returns DataFrame to the original returns DataFrame
combined_portfolios["MY PORTFOLIO"] = my_portfolio_returns
combined_portfolios.head()


# In[54]:


# Only compare dates where return data exists for all the stocks (drop NaNs)
combined_portfolios.dropna(inplace=True)
combined_portfolios.head()


# In[57]:


# Calculate the annualized `std`
combined_portfolios.std()


# In[59]:


# Calculate rolling standard deviation
combined_portfolios.rolling(window=30).mean()


# In[61]:


# Plot rolling standard deviation
combined_portfolios.rolling(window=30).std().plot(figsize=(15, 7.5))


# In[65]:


# Calculate the correlation
calculated_correlation = combined_portfolios.corr()
# Plot the correlation

calculated_correlation.style.background_gradient(cmap='coolwarm')


# In[66]:


# Calculate covariance of my portfolio
covariance = combined_portfolios["MY PORTFOLIO"].rolling(window=30).cov(combined_portfolios["S&P tsx 60"])


# In[67]:


# Calculate variance of S&P TSX
variance = combined_portfolios["S&P tsx 60"].rolling(window=30).var()


# In[69]:


# Calculate Beta
my_portfolio_beta = covariance / variance


# In[70]:


# Plot beta trend
my_portfolio_beta.plot(figsize=(15, 7.5))


# In[71]:


# Calculate Annualized Sharpe Ratios
sharpe_ratio = (combined_portfolios.mean() * 252) / (combined_portfolios.std() * np.sqrt(252))


# In[72]:


# Visualize the sharpe ratios as a bar plot
sharpe_ratio.plot(kind="bar")


# In[76]:


# how does portfolio do
print("My portfolio seemed to do well in relation to other holdings in the combined portfolio, ranking in a third position. This was pre Covid so I am sure the outcome would be much different during Covid")


# In[ ]:




