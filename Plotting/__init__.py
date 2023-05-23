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
