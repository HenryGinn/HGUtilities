import os
import math

import matplotlib.pyplot as plt
import numpy as np

import Defaults as defaults
from Plotting.PlotTypes.PlotLines import PlotLines
from Plotting.PlotTypes.PlotBars import PlotBars
from Plotting.PlotTypes.PlotPie import PlotPie
from Plotting.PlotTypes.PlotColormap import PlotColormap
from Plotting.PlotTypes.PlotSurface import PlotSurface
from Plotting.PlotUtils.GridDimensions import get_grid_dimensions
from Plotting.PlotUtils.SaveFigure import save_figure

class Figure():

    """
    An instance of Plot will be a single figure.
    This figure can have multiple subplots, and corresponding to
    each subplot is a Lines object. A Lines object has a collection
    of Line objects associated with it.
    """

    def __init__(self, figures_obj, data_objects, plot_index):
        self.figures_obj = figures_obj
        self.plot_index = plot_index
        self.initialise_data_objects(data_objects)
        self.set_grid_size()
        self.set_plot_classes()

    def set_plot_classes(self):
        self.plot_classes = {"Lines": PlotLines,
                             "Bars": PlotBars,
                             "Pie": PlotPie,
                             "Colormap": PlotColormap,
                             "Surface": PlotSurface}

    def initialise_data_objects(self, data_objects):
        self.data_objects = data_objects
        self.count = len(data_objects)
        if self.figures_obj.universal_legend:
            self.count += 1

    def set_grid_size(self):
        aspect_ratio = self.figures_obj.aspect_ratio
        self.rows, self.columns = get_grid_dimensions(self.count, aspect_ratio)

    def create_figure(self):
        self.initialise_figure()
        self.create_plots()
        self.add_figure_peripherals()
        self.output_figure()
        plt.close()

    def initialise_figure(self):
        self.create_axes()
        self.remove_extra_axes()

    def create_axes(self):
        self.fig = plt.figure(constrained_layout=True)
        self.axes = [self.get_axis(index, data_obj)
                     for index, data_obj in enumerate(self.data_objects)]

    def get_axis(self, index, data_obj):
        axis = self.fig.add_subplot(self.rows, self.columns, index + 1,
                                    projection=data_obj.projection)
        return axis
    
    def remove_extra_axes(self):
        extra_axes_count = len(self.axes) - self.count
        for ax, _ in zip(self.axes[::-1], range(extra_axes_count)):
            ax.remove()

    def add_figure_peripherals(self):
        self.set_suptitle()
        self.set_universal_legend()

    def set_suptitle(self):
        if self.figures_obj.title is not None:
            self.fig.suptitle(f"{self.figures_obj.title}")

    def set_universal_legend(self):
        if self.figures_obj.universal_legend:
            self.do_universal_legend()

    def do_universal_legend(self):
        ax = self.axes[-1]
        for data_obj in self.data_objects[0].data_objects:
            ax.plot(1, 1, label=data_obj.label, color=data_obj.colour)
        ax.legend(loc="center", borderpad=2, labelspacing=1)
        ax.axis("off")

    def create_plots(self):
        self.plot_objects = [self.create_plot_obj(ax, data_obj)
                             for ax, data_obj in zip(self.axes, self.data_objects)]

    def create_plot_obj(self, ax, data_obj):
        plot_class = self.plot_classes[data_obj.__class__.__name__]
        plot_obj = plot_class(self, ax, data_obj)
        plot_obj.create_plot()
        return plot_obj
    
    def output_figure(self):
        if self.figures_obj.output == "Show":
            plt.show()
        elif self.figures_obj.output == "Save":
            save_figure(self)

defaults.load(Figure)
