
# coding: utf-8

# # References: <br>
# https://bokeh.pydata.org/en/latest <br>
# https://www.journaldev.com/19527/bokeh-python-data-visualization

# In[1]:

# installing library

from bokeh.plotting import figure, output_file, show


# In[6]:

output_file("Intro_bokeh.html")
plot = figure()
plot.line([1, 2, 3, 4, 5], [3,6,9,3,6 ], line_width=2)
show(plot)


# adding titles and labels

# In[ ]:

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("Intro_bokeh.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# show the results
show(p)


# In[1]:

# plotting map of new jersey 

import bokeh.sampledata # importing bokeh 
bokeh.sampledata.download() # downloads sample data from bokeh


# In[2]:

from bokeh.io import show # importing show function to display the output
from bokeh.models import (
    ColumnDataSource, 
    HoverTool, # hovertool helps the user to hover over the map and give details
    LogColorMapper # fills the color 
)
from bokeh.palettes import Viridis6 as palette # imports different palettes
from bokeh.plotting import figure # import different figures

from bokeh.sampledata.us_counties import data as counties # importing data of counties
from bokeh.sampledata.unemployment import data as unemployment # importing data of unemployment within counties

palette.reverse() # reverses colors of the palette

counties = {
    code: county for code, county in counties.items() if county["state"] == "nj"
} # specify the coude for county state Nj

county_xs = [county["lons"] for county in counties.values()] # plotting x axis
county_ys = [county["lats"] for county in counties.values()] # plotting y axis

county_names = [county['name'] for county in counties.values()] #  assigning names of county data
county_rates = [unemployment[county_id] for county_id in counties] # assigning unemployment rate of county
color_mapper = LogColorMapper(palette=palette) # using the color mapper funtion to fill the map according to the rates

source = ColumnDataSource(data=dict(
    x=county_xs, # assigining x axis
    y=county_ys, # assigining y axis
    name=county_names,  # naming name
    rate=county_rates, # naming rate
))

TOOLS = "pan,wheel_zoom,reset,hover,save" # tools funtions

p = figure(
    title="Bokeh Map of New Jersey", tools=TOOLS,
    x_axis_location=None, y_axis_location=None # defining x_axis and y axis location as none
)
p.grid.grid_line_color = None # grid_line color is defined as none

p.patches('x', 'y', source=source,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)

hover = p.select_one(HoverTool) # option to select one hover tool
hover.point_policy = "follow_mouse" # hover tool will follow mouse movement
hover.tooltips = [
    ("Name", "@name"),
    ("Unemployment rate)", "@rate%"),
    ("(Long, Lat)", "($x, $y)"),
]

show(p) # shows the output
 


# In[ ]:



