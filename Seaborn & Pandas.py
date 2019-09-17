#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


temp_df = pd.read_csv('temperature.csv')
print(temp_df.head(5))
print(temp_df.tail(5))


# ## Let’s save ourselves 23/24ths of this headache by taking our recorded temperatures down to one reading per day.We’ll modify our DataFrame to only include one out of every 24 rows:

# In[3]:


modified_df = temp_df.iloc[::24]
modified_df.head()


# ## We'll only take data of New York per 24 hrs

# In[4]:


nyc_df = temp_df[['datetime','New York']]
nyc_df = nyc_df.iloc[::24]
nyc_df.dropna(how='any', inplace=True)
print(nyc_df.head(5))
print(nyc_df.tail(5))


# ## Since the temperatures are in kelvin, We'll convert it into Celcius

# In[5]:


nyc_df['New York'] = nyc_df['New York'].apply(lambda x: (x-273.15) * 9/5 + 32)
print(nyc_df.head(5))


# In[6]:


print(nyc_df.info()) # checking data types 


# In[10]:


nyc_df['datetime'] = pd.to_datetime(nyc_df['datetime']) # changing from object to datetime
print(nyc_df.info())


# # Plotting on Graph

# In[16]:


nyc_df['year'] = nyc_df['datetime'].dt.year # adding year
nyc_df['day'] = nyc_df['datetime'].dt.dayofyear # adding days 
print(nyc_df.head())


# In[21]:


nyc_df.columns = ['date','temperature', 'day', 'year'] # Changing column names
print(nyc_df.head())
nyc_df.reset_index(inplace=True)


# In[29]:


sns.palplot(sns.color_palette("husl", 9))


# In[38]:


nyc_chart = sns.lineplot(x="day", y="temperature", hue='year', data=nyc_df ).set_title('NYC Weather Over Time')
plt.show()


# In[ ]:




