
# coding: utf-8

#  Reference: Udemy Python course

# # Choropleth Maps
# 
# A map that uses differences in shading, coloring, or the placing of symbols within predefined areas to indicate the average values of a property or quantity in those areas.

# ## Offline Plotly Usage

# Get imports and set everything up to be working offline.

# In[3]:

import plotly.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# Now set up everything so that the figures show up in the notebook:

# In[4]:

init_notebook_mode(connected=True) 


# In[5]:

import pandas as pd


# Now we need to begin to build our data dictionary. Easiest way to do this is to use the dict() function of the general form:
# 
# type = 'choropleth',
# locations = list of states
# locationmode = 'USA-states'
# colorscale=
# Either a predefined string:
# 
# 'pairs' | 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
# or create a custom colorscale
# 
# text= list or array of text to display per point
# z= array of values on z axis (color of state)
# colorbar = {'title':'Colorbar Title'})
# Here is a simple example:

# In[6]:

data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['text1','text2','text3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})


# Then we create the layout nested dictionary:

# In[7]:

layout = dict(geo = {'scope':'usa'})


# Then we use: 
# 
#     go.Figure(data = [data],layout = layout)
#     
# to set up the object that finally gets passed into iplot()

# In[9]:

choromap = go.Figure(data = [data],layout = layout)


# In[10]:

iplot(choromap)


# ### Real Data US Map Choropleth
# 
# Now let's show an example with some real data as well as some other options we can add to the dictionaries in data and layout.

# In[12]:

df = pd.read_csv('2011_US_AGRI_Exports')
df.head()


# Now out data dictionary with some extra marker and colorbar arguments:

# In[13]:

data = dict(type='choropleth',
            colorscale = 'YIOrRd',
            locations = df['code'],
            z = df['total exports'],
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"Millions USD"}
            ) 


# And our layout dictionary with some more arguments:

# In[14]:

layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )


# In[15]:

choromap = go.Figure(data = [data],layout = layout)


# In[16]:

iplot(choromap)


# # World Choropleth Map
# 
# Now let's see an example with a World Map:

# In[18]:

df = pd.read_csv('2014_World_GDP')
df.head()


# In[19]:

data = dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorbar = {'title' : 'GDP Billions US'},
      ) 


# In[20]:

layout = dict(
    title = '2014 Global GDP',
    geo = dict(
        showframe = False,
        projection = {'type':'Mercator'}
    )
)


# In[21]:

choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)


# In[ ]:



