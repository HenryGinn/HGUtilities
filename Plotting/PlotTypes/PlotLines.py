import matplotlib.pyplot as plt
import numpy as np

import Defaults as defaults
from Plotting.PlotTypes.Plot import Plot

class PlotLines(Plot):

    def __init__(self, figure_obj, ax, lines_obj, **kwargs):
        Plot.__init__(self, figure_obj, ax, lines_obj, **kwargs)
        self.lines_obj = lines_obj
        defaults.kwargs(self, kwargs)

defaults.load(PlotLines)
