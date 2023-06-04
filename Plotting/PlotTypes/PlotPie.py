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
                    explode=pie_obj.explode, colors=pie_obj.colors,
                    hatch=pie_obj.hatch, autopct=pie_obj.autopct,
                    pctdistance=pie_obj.pctdistance, labeldistance=pie_obj.labeldistance,
                    shadow=pie_obj.shadow, startangle=pie_obj.startangle,
                    radius=pie_obj.radius, counterclock=pie_obj.counterclock,
                    wedgeprops=pie_obj.wedgeprops, textprops=pie_obj.textprops,
                    center=pie_obj.center, frame=pie_obj.frame,
                    rotatelabels=pie_obj.rotatelabels, normalize=pie_obj.normalize)

    def set_title(self):
        if self.pie_obj.title is not None:
            self.ax.set_title(self.pie_obj.title)

defaults.load(PlotPie)
