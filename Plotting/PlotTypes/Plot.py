import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np

import Defaults as defaults
from Utils.Dicts import remove_none_values

class Plot():

    @classmethod
    def set_function_dict(cls):
        pass
    
    def __init__(self, figure_obj, ax, data_obj, **kwargs):
        self.set_figure_obj(figure_obj)
        self.ax = ax
        self.data_obj = data_obj
        defaults.kwargs(self, kwargs)
        self.set_font_kwargs()

    def set_font_kwargs(self):
        self.set_title_font_kwargs()
        self.set_axis_font_kwargs()

    def set_title_font_kwargs(self):
        kwargs = {"fontname": self.data_obj.title_fontname,
                  "size": self.data_obj.title_fontsize}
        self.title_font_kwargs = remove_none_values(kwargs)

    def set_axis_font_kwargs(self):
        kwargs = {"fontname": self.data_obj.axis_fontname,
                  "size": self.data_obj.axis_fontsize}
        self.axis_font_kwargs = remove_none_values(kwargs)

    def set_figure_obj(self, figure_obj):
        self.figure_obj = figure_obj
        self.figures_obj = figure_obj.figures_obj

    def create_plot(self):
        self.plot_data()
        self.set_title()
        self.add_legend()
        self.add_axis_labels()

    def set_title(self):
        if self.data_obj.title is not None:
            self.ax.set_title(self.data_obj.title,
                              **self.title_font_kwargs)

    def add_legend(self):
        if not self.figures_obj.universal_legend:
            if self.data_obj.legend:
                self.ax.legend(loc=self.data_obj.loc)

    def add_axis_labels(self):
        pass

    def add_x_label(self):
        if self.data_obj.x_label is not None:
            self.ax.set_xlabel(self.data_obj.x_label,
                               **self.axis_font_kwargs)

    def add_y_label(self):
        if self.data_obj.y_label is not None:
            self.ax.set_ylabel(self.data_obj.y_label,
                               **self.axis_font_kwargs)

    def add_z_label(self):
        if self.data_obj.z_label is not None:
            self.ax.set_zlabel(self.data_obj.z_label,
                               **self.axis_font_kwargs)

defaults.load(Plot)
