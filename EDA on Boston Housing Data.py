
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic('matplotlib inline')
sns.set(style="white", font_scale=0.9)


# EDA

# In[2]:

from sklearn.datasets import load_boston

dataset = load_boston()
boston = pd.DataFrame(dataset.data, columns=dataset.feature_names)
boston['MEDV'] = dataset.target

boston.head()


# In[3]:

boston.isnull().sum()


# In[4]:

boston['MEDV'].describe()


# In[5]:

sns.distplot(boston['MEDV'], bins=30, kde=False)
plt.show()


# In[6]:

sns.heatmap(data=boston.corr().round(2), cmap='coolwarm', annot=True, annot_kws={"size":8})
plt.tight_layout()
plt.show()


# In[7]:

sns.jointplot(boston['MEDV'], boston['LSTAT'], kind='hex')


# In[8]:

sns.kdeplot(boston['MEDV'], boston['LSTAT'], shade=True)


# RM (average number of rooms per dwelling)
# 

# In[9]:

grid = sns.JointGrid(x='RM', y='MEDV', data=boston, space=0, size=6, ratio=50)
grid.plot_joint(sns.regplot, color="b")
grid.plot_marginals(sns.rugplot, color="b", height=4)
plt.show()


# AGE (proportion of owner-occupied units built prior to 1940)
# 

# In[10]:

grid = sns.JointGrid(x='AGE', y='MEDV', data=boston, space=0, size=6, ratio=50)
grid.plot_joint(plt.scatter, color="b")
grid.plot_marginals(sns.rugplot, color="b", height=4)
plt.show()


# RAD (index of accessibility to radial highways)
# 

# In[11]:

sns.violinplot(x='RAD', y='MEDV', data=boston)


# PTRATIO (pupil-teacher ratio by town)
# 

# In[12]:

grid = sns.JointGrid(x='PTRATIO', y='MEDV', data=boston, space=0, size=6, ratio=50)
grid.plot_joint(sns.regplot, color="b")
grid.plot_marginals(sns.rugplot, color="b", height=4)
plt.show()


# LSTAT (% lower status of the population)
# 

# In[13]:

grid = sns.JointGrid(x='LSTAT', y='MEDV', data=boston, space=0, size=6, ratio=50)
grid.plot_joint(sns.regplot, color="b", order=2)
grid.plot_marginals(sns.rugplot, color="b", height=4)
plt.show()


# In[ ]:




# In[ ]:



