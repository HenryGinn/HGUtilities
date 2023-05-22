import matplotlib.pyplot as plt
import numpy as np

import Defaults as defaults
from Plotting.PlotTypes.Plot import Plot

class PlotSurface(Plot):

    def __init__(self, figure_obj, ax, surface_obj, **kwargs):
        Plot.__init__(self, figure_obj, ax, **kwargs)
        self.surface_obj = surface_obj
        defaults.kwargs(self, kwargs)

    def set_title(self):
        if self.surface_obj.title is not None:
            self.ax.set_title(self.surface_obj.title)

defaults.load(PlotSurface)
