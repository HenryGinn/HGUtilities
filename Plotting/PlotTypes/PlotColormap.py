import matplotlib.pyplot as plt
import numpy as np

import Defaults as defaults
from Plotting.PlotTypes.Plot import Plot

class PlotColormap(Plot):

    def __init__(self, figure_obj, ax, colormap_obj, **kwargs):
        Plot.__init__(self, figure_obj, ax, colormap_obj, **kwargs)
        self.colormap_obj = colormap_obj
        defaults.kwargs(self, kwargs)

    def plot_data(self):
        data_obj = self.data_obj
        self.ax.pcolormesh(data_obj.x_mesh, data_obj.y_mesh, data_obj.z_mesh)

    def set_title(self):
        if self.colormap_obj.title is not None:
            self.ax.set_title(self.colormap_obj.title)

defaults.load(PlotColormap)
