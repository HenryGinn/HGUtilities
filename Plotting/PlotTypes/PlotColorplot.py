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
        self.ax.pcolormesh(colorplot_obj.x_mesh, colorplot_obj.y_mesh,
                           colorplot_obj.z_mesh)

defaults.load(PlotColorplot)
