#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# In[39]:


data=pd.read_csv("C:\\Users\\hp\\Desktop\\Unemployment_Rate_upto_11_2020.csv")
data2=pd.read_csv("C:\\Users\hp\\Desktop\\Unemployment in India.csv")
#calling csv file in python


# In[27]:


data.head()


# In[40]:


data2.head()


# In[28]:


data.tail()


# In[41]:


data2.tail()


# In[29]:


data.shape
#returns tuple of shape (Rows,Columns) of dataframe


# In[43]:


data2.shape


# In[30]:


data.info()
#print dataframe info


# In[44]:


data2.info()


# In[31]:


data.describe()
#provide numerical description of the data in dataframe


# In[45]:


data2.describe()


# In[46]:


data.isnull().sum()
#returns the cost of null values(mising or undifined data) in each column


# In[47]:


data2.isnull().sum()


# In[48]:


#dropping null values
data=data.dropna()


# In[49]:


data.isnull().sum()


# In[51]:


data2.isna().sum()


# In[52]:


data.duplicated().sum()


# In[54]:


data2.duplicated().sum()


# In[65]:


#state with highest unemployment
data2['Region'].value_counts().idxmax()


# In[61]:


data2['Region'].value_counts()


# In[66]:


data['Region'].value_counts().idxmax()


# In[63]:


#state with lowest unemployment
data2['Region'].value_counts().idxmin()


# In[67]:


data['Region'].value_counts().idxmin()


# In[22]:


x=data['Region']


# In[23]:


x


# In[24]:


y=data[' Estimated Unemployment Rate (%)']


# In[15]:


y


# In[73]:


datam=data.iloc[:,3]


# In[74]:


datam


# In[34]:


fig=px.bar(data,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
           title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[35]:


fig=px.bar(data,x='Region.1',y=' Estimated Unemployment Rate (%)',color='Region',
           title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[36]:


fig=px.box(data,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
           title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[37]:


fig=px.scatter(data,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
           title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[38]:


fig=px.histogram(data,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
           title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[68]:


x1=data2['Region']


# In[69]:


x1


# In[70]:


y1=data2[' Estimated Unemployment Rate (%)']


# In[71]:


y1


# In[75]:


datap=data2.iloc[:,3]


# In[76]:


datap


# In[77]:


fig=px.bar(data2,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
           title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[78]:


fig=px.histogram(data2,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
           title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[ ]:




