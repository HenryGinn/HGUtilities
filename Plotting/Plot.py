import os
import math

import matplotlib.pyplot as plt
import numpy as np

from Plotting.PlotShape import PlotShape
from Plotting.PlotAxes import PlotAxes

class Plot():

    """
    An instance of Plot will be a single figure.
    This figure can have multiple subplots, and corresponding to
    each subplot is a Lines object. A Lines object has a collection
    of Line objects associated with it.
    """

    def __init__(self, plots_obj, lines_objects, plot_index):
        self.plots_obj = plots_obj
        self.plot_index = plot_index
        self.initialise_lines_objects(lines_objects)
        self.set_grid_size()

    def initialise_lines_objects(self, lines_objects):
        self.lines_objects = lines_objects
        self.count = len(self.lines_objects)
        if self.plots_obj.universal_legend:
            self.count += 1

    def set_grid_size(self):
        plot_shape_obj = PlotShape(self.count, self.aspect_ratio)
        self.rows, self.columns = plot_shape_obj.dimensions

    def create_figure(self):
        self.initialise_figure()
        self.populate_figure()
        self.output_figure()
        plt.close()

    def initialise_figure(self):
        self.fig, self.axes = plt.subplots(nrows=self.rows,
                                           ncols=self.columns)
        self.flatten_axes()
    
    def flatten_axes(self):
        if isinstance(self.axes, np.ndarray):
            self.axes = self.axes.flatten()
        else:
            self.axes = [self.axes]

    def populate_figure(self):
        self.plot_axes()
        self.remove_extra_axes()
        self.add_plot_peripherals()
    
    def plot_axes(self):
        for ax, lines_obj in zip(self.axes, self.lines_objects):
            self.plot_lines(ax, lines_obj)
            self.set_subplot_labels(ax, lines_obj)

    def plot_lines(self, ax, lines_obj):
        plot_function = self.get_plot_function(ax, lines_obj)
        for line_obj in lines_obj.line_objects:
            self.plot_line(ax, line_obj, plot_function)

    def get_plot_function(self, ax, lines_obj):
        plot_functions = {"plot": ax.plot,
                          "semilogy": ax.semilogy}
        plot_function = plot_functions[lines_obj.plot_type]
        return plot_function
        
    def plot_line(self, ax, line_obj, plot_function):
        plot_function(line_obj.x_values, line_obj.y_values,
                      color=line_obj.colour,
                      marker=line_obj.marker,
                      linestyle=line_obj.linestyle,
                      linewidth=line_obj.linewidth,
                      label=line_obj.label)

    def set_subplot_labels(self, ax, lines_obj):
        self.set_title(ax, lines_obj)
        self.set_x_axis_label(ax, lines_obj)
        self.set_y_axis_label(ax, lines_obj)

    def set_title(self, ax, lines_obj):
        if hasattr(lines_obj, "title"):
            ax.set_title(lines_obj.title)

    def set_x_axis_label(self, ax, lines_obj):
        if lines_obj.x_label is not None:
            ax.set_xlabel(lines_obj.x_label)

    def set_y_axis_label(self, ax, lines_obj):
        if lines_obj.y_label is not None:
            ax.set_ylabel(lines_obj.y_label)

    def remove_extra_axes(self):
        extra_axes = len(self.axes) - self.count
        for ax, _ in zip(self.axes[::-1], range(extra_axes)):
            ax.remove()

    def add_plot_peripherals(self):
        self.set_suptitle()
        self.set_legend()

    def set_suptitle(self):
        if hasattr(self.plots_obj, "title"):
            self.fig.suptitle(f"{self.plots_obj.title}")

    def set_legend(self):
        if self.plots_obj.universal_legend:
            self.do_universal_legend()
        else:
            self.do_non_universal_legends()

    def do_universal_legend(self):
        ax = self.axes[-1]
        for line_obj in self.lines_objects[0].line_objects:
            ax.plot(1, 1, label=line_obj.label, color=line_obj.colour)
        ax.legend(loc="center", borderpad=2, labelspacing=1)
        ax.axis("off")

    def do_non_universal_legends(self):
        for ax, lines_obj in zip(self.axes, self.lines_objects):
            if lines_obj.legend:
                ax.legend(loc=lines_obj.legend_loc)

    def output_figure(self):
        if self.output == "Show":
            plt.show()
        else:
            self.save_figure()

    def save_figure(self):
        path = self.get_figure_path()
        plt.savefig(self.path, format=self.format)

    def get_figure_path(self):
        file_name = self.get_file_name()
        path = os.path.join(self.plots_obj.path, file_name)
        return path

    def get_file_name(self):
        if len(self.plots_obj.lines_object_groups) == 1:
            return self.get_base_file_name()
        else:
            return self.get_numbered_file_name()

    def get_base_file_name(self):
        if self.title is None:
            return "Figure"
        else:
            return str(self.title)

    def get_numbered_file_name(self):
        file_name = self.get_base_file_name()
        file_name = f"{file_name} {self.plot_index + 1}"
        return file_name
