# Visualization-in-Python
We will be using various Python libraries to interactively visualize the data.

# 1.Bokeh
- Bokeh is an interactive Python data visualization library which targets modern web browsers for presentation. 
- Bokeh aims at providing high-performing interactivity with the concise construction of novel graphics over very large or even streaming datasets in a quick, easy way and elegant manner.

## Bokeh offers simple, flexible and powerful features and provides two interface levels:

1.Bokeh.models: A low-level interface which provides the application developers with most flexibility. <br>
2.Bokeh.plotting: A higher-level interface to compose visual glyphs.

## Bokeh Dependencies
- Before beginning with Bokeh, we need to have NumPy installed on our machine.

## To install using pip open the terminal and run the following command:

- sudo pip install bokeh

# 2. Wordcloud 

- Many times you might have seen a cloud filled with lots of words in different sizes, which represent the frequency or the importance of each word. This is called Tag Cloud or WordCloud. 

## Prerequisites:

You will need to install some packages below:

- numpy <br>
- pandas <br>
- matplotlib <br>
- pillow <br>
- wordcloud  

# 3. Geoplotlib
- Geoplotlib is a toolbox for creating maps and plotting geographical data. You can use it to create a variety of map-types, like choropleths, heatmaps, and dot density maps. You must have Pyglet (an object-oriented programming interface) installed to use geoplotlib. Nonetheless, since most Python data visualization libraries don’t offer maps, it’s nice to have a library dedicated solely to them.

## Geoplotlib requires:

a. numpy

b. pyglet 1.2.4
note: in order for pyglet to work with ipython on Mac, version 1.2.4 or newer is needed

## optional requirements:

c. matplotlib for colormaps

d. scipy for some layers

e. pyshp for reading .shp files

## To install from source run:

- python setup.py install

## or with pip:

- pip install geoplotlib


# 4. Choropleth Maps
- A map that uses differences in shading, coloring, or the placing of symbols within predefined areas to indicate the average values of a property or quantity in those areas.

# 5. Plotly-Express 
- Plotly Express is a new high-level Python visualization library: it’s wrapper for Plotly.py that exposes a simple syntax for complex charts. Inspired by Seaborn and ggplot2, it was specifically designed to have a terse, consistent and easy-to-learn API: with just a single import, you can make richly interactive plots in just a single function call, including faceting, maps, animations, and trendlines.

# 6. Turtle
- Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966.

- Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an import turtle, give it the command turtle.forward(15), and it moves (on-screen!) 15 pixels in the direction it is facing, drawing a line as it moves. Give it the command turtle.right(25), and it rotates in-place 25 degrees clockwise.

#import turtle
