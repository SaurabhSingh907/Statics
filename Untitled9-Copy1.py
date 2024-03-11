#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd


# In[7]:


data = {'Name': ['humble', 'jeetu', 'saurabh'],
        'City': ['delhi', 'mumbai', 'jaipur']}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)


# In[8]:


# creating a series from a list
data = ['P','A','N','D','A','S']
my_series = pd.Series(data)

# display the Series
print("Series:")
print(my_series)


# In[18]:


# create a sample series
data = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
series = pd.Series(data)
mapping = {'A': 'apple', 'B': 'banana', 'C': 'cherry', 'D': 'date'}

result_series = series.map(mapping)

# print the original and mapped Series
print("Original Series:")
print(series)
print("\nMapped Series:")
print(result_series)


# In[17]:


# creating a pandas series
data = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
series = pd.Series(data, name='Values')

# converting the series to a dataframe
dataframe = series.to_frame()

# displaying the dataframe
print(dataframe)


# In[21]:


#creating empty datframe
df=pd.DataFrame()
print(df)


# In[ ]:





# In[ ]:




