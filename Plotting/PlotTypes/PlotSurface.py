import matplotlib.pyplot as plt
import numpy as np

import Defaults as defaults
from Plotting.PlotTypes.Plot import Plot

class PlotSurface(Plot):

    @classmethod
    def set_function_dict(cls):
        cls.function_dict = {"plot_surface": cls.plot_regular}

    def __init__(self, figure_obj, ax, data_obj, **kwargs):
        Plot.__init__(self, figure_obj, ax, data_obj, **kwargs)
        defaults.kwargs(self, kwargs)

    def plot_data(self):
        function_type = self.get_plot_function()
        plot_function = getattr(self.ax, self.data_obj.plot_type)
        function_type(self, plot_function, self.data_obj)
        self.set_z_limits()
        self.set_axes()

    def get_plot_function(self):
        plot_type = self.data_obj.plot_type
        plot_function = self.function_dict[plot_type]
        return plot_function

    def plot_regular(self, plot_function, data_obj):
        plot_function(data_obj.x_values, data_obj.y_values, data_obj.z_values,
                      cmap=data_obj.cmap, vmin=data_obj.z_limits[0], vmax=data_obj.z_limits[1])

    def set_z_limits(self):
        if self.data_obj.z_limits is not None:
            bottom, top = self.data_obj.z_limits
            self.ax.set_zlim(bottom=bottom, top=top)

    def set_axes(self):
        if not self.data_obj.axes:
            self.ax.axis("off")

defaults.load(PlotSurface)
