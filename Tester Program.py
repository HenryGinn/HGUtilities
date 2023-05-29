import Plotting as plotting

from Plotting.Animate import Animate
help(Animate)

# Importing
import numpy as np
#import hgutils.plotting

# Creating bars object
x_values_1 = ["Red", "Green", "Blue"]
y_values_1 = [4, 2, 7]
bar_obj_1 = plotting.bar(x_values_1, y_values_1)

x_values_2 = ["Green", "Red", "Blue"]
y_values_2 = [1, 4, 5]
bar_obj_2 = plotting.bar(x_values_2, y_values_2)

title = "Bar Chart Example"
bar_objects = [bar_obj_1, bar_obj_2]
bars_obj = plotting.bars(bar_objects, title=title)

# Creating pie object
values = [4, 2, 7]
labels = ["Red", "Green", "Blue"]
title = "Pie Chart Example"
pie_obj = plotting.pie(values, labels, title=title,
                       colors=labels)

#data_objects = [bars_obj], pie_obj, surface_obj, colormap_obj]
data_objects = [pie_obj]

# Creation of figures
#plotting.create_figures(data_objects)

