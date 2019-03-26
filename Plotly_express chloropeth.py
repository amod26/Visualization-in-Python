#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly_express as px


# In[3]:


gapminder = px.data.gapminder()


# In[4]:


px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year",
             color_continuous_scale=px.colors.sequential.Plasma)


# In[ ]:




