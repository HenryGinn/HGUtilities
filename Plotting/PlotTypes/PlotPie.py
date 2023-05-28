import matplotlib.pyplot as plt
import numpy as np

import Defaults as defaults
from Plotting.PlotTypes.Plot import Plot

class PlotPie(Plot):

    def __init__(self, figure_obj, ax, pie_obj, **kwargs):
        Plot.__init__(self, figure_obj, ax, pie_obj, **kwargs)
        self.pie_obj = pie_obj
        defaults.kwargs(self, kwargs)

    def plot_data(self):
        pie_obj = self.pie_obj
        self.ax.pie(pie_obj.values, labels=pie_obj.labels,
                    colors=pie_obj.color)

    def set_title(self):
        if self.pie_obj.title is not None:
            self.ax.set_title(self.pie_obj.title)

defaults.load(PlotPie)
