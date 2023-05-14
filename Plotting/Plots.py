import os
import __main__

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
        self.lines_obj_count = self.lines_objects.size
    
    def plot(self):
        self.process_lines_objects()
        self.process_output_mode()
        self.plot_lines_objects()

    def process_output_mode(self):
        if self.output == "Save":
            self.create_plots_folder()

    def create_plots_folder(self):
        if self.path is None:
            self.path = os.path.split(__main__.__file__)[0]
        make_folder(self.path)

    def process_lines_objects(self):
        self.subplots = get_group_size(self.subplots, self.lines_objects)
        group_indexes = get_group_indexes(self.lines_obj_count, self.subplots)
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
