import os
import __main__
import PIL
import io

import numpy as np
from matplotlib.pyplot import savefig
from matplotlib.pyplot import show

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
    
    def create_figures(self):
        self.process_data_objects()
        self.process_output_mode()
        self.plot_data_objects()

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

    def plot_data_objects(self):
        self.set_figure_objects()
        for figure_obj in self.figure_objects:
            figure_obj.create_figure()

    def set_figure_objects(self):
        data_obj_iterable = enumerate(self.data_object_groups)
        self.figure_objects = [Figure(self, data_object_group, index)
                               for index, data_object_group in data_obj_iterable]

    def create_animations(self):
        self.process_data_objects()
        self.set_figure_objects()
        self.prepare_animation_settings()
        self.animate_data_objects()

    def prepare_animation_settings(self):
        self.output = None
        self.set_animation_axis_limits()

    def set_animation_axis_limits(self):
        for figure_obj in self.figure_objects:
            figure_obj.set_animation_axis_limits()

    def animate_data_objects(self):
        self.set_figure_objects()
        for figure_obj in self.figure_objects:
            self.animate_figure(figure_obj)

    def animate_figure(self, figure_obj):
        frame_count = figure_obj.get_frame_count()
        self.set_all_data_values(figure_obj)
        frames = [self.get_frame(figure_obj, index)
                  for index in range(frame_count)]
        frames[0].save("My animation.gif", loop=0, save_all=True,
                       append_images=frames[1:], duration=80)

    def set_all_data_values(self, figure_obj):
        figure_obj.all_data_values = [data_obj.get_data_values()
                                      for data_obj in figure_obj.data_objects]

    def get_frame(self, figure_obj, index):
        figure_obj.set_data_value(index)
        figure_obj.create_figure()
        buffer = io.BytesIO()
        savefig(buffer, bbox_inches="tight")
        buffer.seek(0)
        image = PIL.Image.open(buffer)
        return image

defaults.load(Figures)
