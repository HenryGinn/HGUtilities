# Plotting

## Overview and Structure

This is a tool designed to make creating figures with multiple subplots easier. The data is prescribed, and the creation of the figures is handled by the package.

### Figures

At the top level there is a Figures object. This contains all the information about the figures to be produced. This includes the data to be plotted, the title of the figures, if the figures are going to be shown or saved, the base path to be saved to if needed, the number of subplots per figure, and any appearance settings of the plots. It organises the creation of Figure objects, as if there is too much data for one figure, it will need to be splot over multiple.

### Figure

The next level down is the Figure object. This arranges how the subplots will be arranged on the figure and organises the creation of the subplots which are handled by Plot objects. Adding the title and universal legend happens here. An aspect ratio can be specified, and it will try to arrange the plots to that ratio as closely as it can.

### Plot

A Plot object is responsible for each individual subplot. The subplot title, axis labels, plot legends, and the data to be put on the subplot are handled at this level. There are subclasses of Plot for different types of plot. The most basic is a Lines object which handles quantititive data on a 2D plot. There is also a Bars object which handles bar charts, and a Pie object that handles pie charts. Colormesh and Surface are also subclasses which work with 3 dimensional data. As a rule of thumb, if two matplotlib plotting functions are sufficiently different, they will be handled by two distinct subclasses.

- Lines. This takes in a collection of Line objects. It also has an optional keyword argument called plot_type which controls whether the plot is made using plot, semilogy, semilogx, loglog, or errorbar. Each Line object corresponds to a single line on a subplot, and has a list of x_values and y_values. The Line object has attributes that control the appearance of the line and the line label.
- Bars. This is similar to Lines, but it handles Bar objects which are similar to Line objects. The key distinction here is that the $x$ axis has qualitative data, and that prescribing the appearance of the bars is very different from lines. We note that a Bar object handles an entire series of data, and a Bars object handles a bar chart plot, so a single plot with two data series on it will be handled by one Bars object and two Bar objects.
- Pie. Pie charts cannot show multiple data series so this subclass does not have a correspondence to Line or Bar. This takes in all the arguments that the matplotlib pie function takes in, and also any of the arguments from the parent class, Plot.
- Colormesh.
- Surface.

## Features

### Universal Legend

The universal legend is a tool that can be used if all subplots in a figure have the same legend. An extra blank subplot is created and the space is used to show a legend that corresponds to all plots. This can be activated by passing universal_legend=True as a keyword-value pair into the create_figures function, and any individual legends will be overruled.