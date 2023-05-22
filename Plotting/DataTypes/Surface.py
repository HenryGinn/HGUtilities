import numpy as np
from matplotlib.colors import hsv_to_rgb

import Defaults as defaults
from Plotting.DataTypes.Data import Data

class Surface(Data):

    def __init__(self, x_values, y_values, z_values, **kwargs):
        Data.__init__(self, **kwargs)
        self.set_xyz_values(x_values, y_values, z_values)
        defaults.kwargs(self, kwargs)

    def set_xyz_values(self, x_values, y_values, z_values):
        self.x_values = x_values
        self.y_values = y_values
        self.z_values = z_values

defaults.load(Surface)
