import numpy as np
from matplotlib.colors import hsv_to_rgb

import Defaults as defaults

class Lines():

    def __init__(self, line_objects, **kwargs):
        defaults.kwargs(self, kwargs)
        self.line_objects = line_objects
        self.count = len(line_objects)

    def set_rainbow_lines(self, saturation=1, value=1):
        self.set_colours(saturation, value)
        for line_obj, colour in zip(self.line_objects, self.colours):
            line_obj.colour = colour

    def set_colours(self, saturation, value):
        hues = np.linspace(0, 1, self.count + 1)[:self.count]
        saturations = np.ones(self.count)*saturation
        values = np.ones(self.count)*value
        hsv_tuples = np.array(list(zip(hues, saturations, values)))
        self.colours = hsv_to_rgb(hsv_tuples)

defaults.load(Lines)
