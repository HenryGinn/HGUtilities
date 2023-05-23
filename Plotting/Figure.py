import os
import math
from screeninfo import get_monitors

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
from Plotting.PlotUtils.FigureSize import maximise_figure

class Figure():

    """
    An instance of Plot will be a single figure.
    This figure can have multiple subplots, and corresponding to
    each subplot is a Lines object. A Lines object has a collection
    of Line objects associated with it.
    """

    @classmethod
    def set_plot_classes(cls):
        cls.plot_classes = {"Lines": PlotLines,
                            "Bars": PlotBars,
                            "Pie": PlotPie,
                            "Colormap": PlotColormap,
                            "Surface": PlotSurface}
    
    def __init__(self, figures_obj, data_objects, plot_index, **kwargs):
        defaults.kwargs(self, kwargs)
        self.figures_obj = figures_obj
        self.plot_index = plot_index
        self.initialise_data_objects(data_objects)
        self.set_grid_size()
        self.process_light_or_dark()

    def process_light_or_dark(self):
        if self.dark:
            plt.style.use('dark_background')

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

    def initialise_figure(self):
        self.create_axes()
        self.remove_extra_axes()

    def create_axes(self):
        self.fig = plt.figure(constrained_layout=True, dpi=self.dpi)
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
        self.set_figure_size()

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

    def set_figure_size(self):
        self.update_size()
        self.set_figure_size_pixels()

    def update_size(self):
        if self.maximise:
            self.maximise_figure()
        else:
            self.set_figure_inches()

    def maximise_figure(self):
        maximise_figure()
        monitor = get_monitors()[0]
        figure_size = [monitor.width_mm / 25.4, monitor.height_mm / 25.4]
        self.fig.set_size_inches(figure_size)

    def set_figure_inches(self):
        if self.figure_size is not None:
            self.fig.set_size_inches(self.figure_size)

    def set_figure_size_pixels(self):
        if self.maximise:
            self.set_figure_size_pixels_maximise()
        else:
            self.set_figure_size_pixels_unmaximise()

    def set_figure_size_pixels_maximise(self):
        window = plt.get_current_fig_manager().window
        self.figure_size_pixels = list(window.wm_maxsize())
        self.figure_size_pixels[0] //= 2

    def set_figure_size_pixels_unmaximise(self):
        self.figure_size_pixels = self.fig.get_size_inches()*self.fig.dpi
        self.figure_size_pixels = [int(value) for value in self.figure_size_pixels]

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
            self.show_figure()
        elif self.figures_obj.output == "Save":
            save_figure(self)

    def show_figure(self):
        plt.show()
        plt.close()

    def set_animation_axis_limits(self):
        for data_obj in self.data_objects:
            data_obj.set_animation_axis_limits()

    def get_frame_count(self):
        frame_count = self.data_objects[0].get_frame_count()
        return frame_count

    def set_data_value(self, index):
        for data_obj, data_values in zip(self.data_objects, self.all_data_values):
            data_value = data_values[index]
            data_obj.set_data_value(data_value)

defaults.load(Figure)
