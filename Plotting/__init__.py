"""
Plotting

This is a module is an interface for matplotlib and is designed to make
creation and processing of figures with subplots easier. The data and
settings are specified, and they are arranged on figures where the user
can control the maximum number of subplots on each figure and prescribe
a target aspect ratio. If the subplots do not fit on one figure, they
will be spread over multiple figures. The number of figures is no more
than the ceiling of the total number of plots divided by the maximum
number of plots per figure.

While this module offers a lot of flexibility, it is mainly intended for
convenient production of figures. For publication quality plots, it is
recommended that the full flexibility of matplotlib or other plotting
packages should be used instead. This module performs best for purposes
such as analysing data, and making powerpoints to be shared among
colleages and students.

Functions defined here:

create_figures
create_animations

For further documentation see the following:
Data and Figures classes and functions from the above list
https://github.com/HenryGinn/HGUtils
https://github.com/HenryGinn/HGUtils/tree/main/Plotting
"""

import os
import sys
package_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(package_path)

import Defaults as defaults

from Plotting.PlotFunctions import create_figures
from Plotting.PlotFunctions import create_animations
from Plotting.Figure import Figure
from Plotting.DataTypes.Line import Line as line
from Plotting.DataTypes.Lines import Lines as lines
from Plotting.DataTypes.Bars import Bars as bars
from Plotting.DataTypes.Bar import Bar as bar
from Plotting.DataTypes.Pie import Pie as pie
from Plotting.DataTypes.Surface import Surface as surface
from Plotting.DataTypes.Colormap import Colormap as colormap
from Plotting.PlotTypes.PlotLines import PlotLines
from Plotting.PlotTypes.PlotBars import PlotBars
from Plotting.PlotTypes.PlotPie import PlotPie
from Plotting.PlotTypes.PlotSurface import PlotSurface
from Plotting.PlotTypes.PlotColormap import PlotColormap

Figure.set_plot_classes()
PlotLines.set_function_dict()
PlotBars.set_function_dict()
PlotPie.set_function_dict()
PlotSurface.set_function_dict()
PlotColormap.set_function_dict()
