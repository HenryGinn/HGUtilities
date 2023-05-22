import matplotlib.pyplot as plt
import numpy as np

import Defaults as defaults

class Plot():

    def __init__(self, figure_obj, ax, data_obj, **kwargs):
        self.figure_obj = figure_obj
        self.ax = ax
        self.data_obj = data_obj
        defaults.kwargs(self, kwargs)

    def create_plot(self):
        self.set_title()

    def set_title(self):
        if self.data_obj.title is not None:
            self.ax.set_title(self.data_obj.title)

defaults.load(Plot)
