

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


df=pd.read_csv('/Users/ulugbek_turaev/Downloads/USA_cars_datasets.csv')
df.head()


# In[14]:


df.drop(['Unnamed: 0','vin'],axis=1,inplace=True)
df.head()


# In[15]:


df.hist()


# In[16]:


plt.hist(df['price'], color = 'blue', edgecolor = 'black',bins=10)

# Add labels
plt.title('Range of prices')
plt.xlabel('Prices')
plt.ylabel('No. of cars')


# In[19]:


plt.hist(df['country'], color = 'purple', edgecolor = 'green',bins=6)


# In[20]:


plt.figure(figsize=(12,6))
sorted_nb = df.groupby(['brand'])['price'].median().sort_values()
sns.boxplot(x=df['brand'], y=df['price'], order=list(sorted_nb.index))
plt.xticks(rotation=70)


# In[21]:


df['state'].value_counts().head(30).plot(kind='barh', figsize=(6,10))


# In[22]:


plt.figure(figsize=(15,8))
sns.countplot(df['color']);
plt.xticks(rotation=90)


# In[23]:





# In[ ]:




