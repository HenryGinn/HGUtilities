import os
import __main__

import numpy as np

import Defaults as defaults
from Plotting.Figure import Figure
from Utils.Groups import get_group_indexes
from Utils.Groups import get_group_size
from Utils.Paths import make_folder

class Figures():

    """
    An instance of Plots will represent several figures that are
    all associated with one list of objects. When wanting to plot
    multiple things, they might not all fit on one figure. Plots
    organises how they are put onto multiple figures, and each of
    those figures is handled as a single Plot object.
    """

    def __init__(self, data_objects, **kwargs):
        defaults.kwargs(self, **kwargs)
        self.data_objects = np.array(data_objects)
        self.data_obj_count = self.data_objects.size
    
    def create_figures(self, **kwargs):
        self.process_data_objects()
        self.process_output_mode()
        self.plot_data_objects(**kwargs)

    def process_output_mode(self):
        if self.output == "Save":
            self.create_plots_folder()

    def create_plots_folder(self):
        if self.path is None:
            self.path = os.path.split(__main__.__file__)[0]
        make_folder(self.path)

    def process_data_objects(self):
        self.subplots = get_group_size(self.subplots, self.data_objects)
        group_indexes = get_group_indexes(self.data_obj_count, self.subplots)
        self.data_object_groups = [self.data_objects[indexes]
                                    for indexes in group_indexes]

    def plot_data_objects(self, **kwargs):
        self.set_figure_objects(**kwargs)
        for figure_obj in self.figure_objects:
            figure_obj.create_figure()

    def set_figure_objects(self, **kwargs):
        data_obj_iterable = enumerate(self.data_object_groups)
        self.figure_objects = [Figure(self, data_object_group, index, **kwargs)
                               for index, data_object_group in data_obj_iterable]


defaults.load(Figures)
