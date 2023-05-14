import os

import numpy as np

import Defaults as defaults
from Plotting.Plot import Plot
from Utils.Groups import get_group_indexes
from Utils.Groups import get_group_size
from Utils.Paths import make_folder

class Plots():

    """
    An instance of Plots will represent several figures that are
    all associated with one list of objects. When wanting to plot
    multiple things, they might not all fit on one figure. Plots
    organises how they are put onto multiple figures, and each of
    those figures is handled as a single Plot object.
    """

    def __init__(self, lines_objects, **kwargs):
        defaults.kwargs(self, **kwargs)
        self.lines_objects = np.array(lines_objects)
    
    def plot(self):
        self.process_lines_objects()
        self.process_output_mode()
        self.plot_lines_objects()

    def process_output_mode(self):
        if self.output == "Save":
            self.create_plots_folder()

    def create_plots_folder(self):
        if hasattr(self.plots_obj, "path"):
            return make_folder(self.plots_obj.path)
        else:
            raise Exception(f"Plots '{self.plots_obj.title}' has no path set")

    def process_lines_objects(self):
        self.subplots = get_group_size(subplots, self.lines_objects)
        group_indexes = get_group_indexes(self.total, self.subplots)
        self.lines_object_groups = [self.lines_objects[indexes]
                                    for indexes in group_indexes]

    def plot_lines_objects(self):
        self.set_plot_objects()
        for plot_obj in self.plot_objects:
            plot_obj.create_figure()

    def set_plot_objects(self):
        lines_iterable = enumerate(self.lines_object_groups)
        self.plot_objects = [Plot(self, lines_object_group, index)
                             for index, lines_object_group in lines_iterable]

defaults.load(Plots)

def plot(lines_objects, **kwargs):
    plots_obj = Plots(lines_objects, **kwargs)
    plots_obj.plot()
    return plots_obj
