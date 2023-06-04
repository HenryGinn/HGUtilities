# Allowing the package to access the rest of the package
import os
import sys
package_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(package_path)

import Defaults as defaults

# Functions and classes to be accessed by the user
from Plotting.PlotFunctions import create_figures
from Plotting.PlotFunctions import create_animations
from Plotting.DataTypes.Line import Line
from Plotting.DataTypes.Lines import Lines
from Plotting.DataTypes.Bars import Bars
from Plotting.DataTypes.Bar import Bar
from Plotting.DataTypes.Pie import Pie
from Plotting.DataTypes.Surface import Surface
from Plotting.DataTypes.Colorplot import Colorplot

# Classes that need initialisation
from Plotting.Figure import Figure
from Plotting.PlotTypes.PlotLines import PlotLines
from Plotting.PlotTypes.PlotBars import PlotBars
from Plotting.PlotTypes.PlotPie import PlotPie
from Plotting.PlotTypes.PlotSurface import PlotSurface
from Plotting.PlotTypes.PlotColorplot import PlotColorplot

# Initialising classes
Figure.set_plot_classes()
PlotLines.set_function_dict()
PlotBars.set_function_dict()
PlotPie.set_function_dict()
PlotSurface.set_function_dict()
PlotColorplot.set_function_dict()

# Importing other classes that have documentation
# files so they can be detected by defaults.doc
from Plotting.Animate import Animate

defaults.docs()
