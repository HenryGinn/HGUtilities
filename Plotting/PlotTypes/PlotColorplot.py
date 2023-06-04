import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np

import Defaults as defaults
from Plotting.PlotTypes.Plot import Plot

class PlotColorplot(Plot):

    def __init__(self, figure_obj, ax, colorplot_obj, **kwargs):
        Plot.__init__(self, figure_obj, ax, colorplot_obj, **kwargs)
        self.colorplot_obj = colorplot_obj
        defaults.kwargs(self, kwargs)

    def plot_data(self):
        colorplot_obj = self.colorplot_obj
        x_and_y = self.get_x_and_y()
        self.ax.pcolormesh(*x_and_y, colorplot_obj.z_mesh)

    def get_x_and_y(self):
        if ((self.colorplot_obj.x is not None) and
            (self.colorplot_obj.y is not None)):
            return (self.colorplot_obj.x, self.colorplot_obj.y)
        else:
            return ()

defaults.load(PlotColorplot)
