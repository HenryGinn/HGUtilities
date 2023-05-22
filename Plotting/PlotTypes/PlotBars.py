import matplotlib.pyplot as plt
import numpy as np

import Defaults as defaults
from Plotting.PlotTypes.Plot import Plot

class PlotBars(Plot):

    def __init__(self, figure_obj, ax, bars_obj, **kwargs):
        Plot.__init__(self, figure_obj, ax, **kwargs)
        self.bars_obj = bars_obj
        defaults.kwargs(self, kwargs)

    def set_title(self):
        if self.bars_obj.title is not None:
            self.ax.set_title(self.bars_obj.title)

defaults.load(PlotBars)
