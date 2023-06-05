import Defaults as defaults

# Functions and classes to be accessed by the user
from .PlotFunctions import create_figures
from .PlotFunctions import create_animations
from .DataTypes.Line import Line
from .DataTypes.Lines import Lines
from .DataTypes.Bars import Bars
from .DataTypes.Bar import Bar
from .DataTypes.Pie import Pie
from .DataTypes.Surface import Surface
from .DataTypes.Colorplot import Colorplot

# Classes that need initialisation
from .Figure import Figure
from .PlotTypes.PlotLines import PlotLines
from .PlotTypes.PlotBars import PlotBars
from .PlotTypes.PlotPie import PlotPie
from .PlotTypes.PlotSurface import PlotSurface
from .PlotTypes.PlotColorplot import PlotColorplot

# Initialising classes
Figure.set_plot_classes()
PlotLines.set_function_dict()
PlotBars.set_function_dict()
PlotPie.set_function_dict()
PlotSurface.set_function_dict()
PlotColorplot.set_function_dict()

# Importing other classes that have documentation
# files so they can be detected by defaults.doc
from .Animate import Animate

defaults.docs()
