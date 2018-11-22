# Visualization-in-Python
We will be using various Python libraries to interactively visualize the data.

# 1.Bokeh
- Bokeh is an interactive Python data visualization library which targets modern web browsers for presentation. 
- Bokeh aims at providing high-performing interactivity with the concise construction of novel graphics over very large or even streaming datasets in a quick, easy way and elegant manner.

## Bokeh offers simple, flexible and powerful features and provides two interface levels:

1.Bokeh.models: A low-level interface which provides the application developers with most flexibility.
2.Bokeh.plotting: A higher-level interface to compose visual glyphs.

## Bokeh Dependencies
- Before beginning with Bokeh, we need to have NumPy installed on our machine.

## To install using pip open the terminal and run the following command:

- sudo pip install bokeh

# 2. Geoplotlib
- Geoplotlib is a toolbox for creating maps and plotting geographical data. You can use it to create a variety of map-types, like choropleths, heatmaps, and dot density maps. You must have Pyglet (an object-oriented programming interface) installed to use geoplotlib. Nonetheless, since most Python data visualization libraries don’t offer maps, it’s nice to have a library dedicated solely to them.

- geoplotlib requires:
a. numpy

b. pyglet 1.2.4
note: in order for pyglet to work with ipython on Mac, version 1.2.4 or newer is needed

optional requirements:

c. matplotlib for colormaps

d. scipy for some layers

e. pyshp for reading .shp files

## to install from source run:

- python setup.py install

or with pip:

- pip install geoplotlib
