import numpy as np

import Defaults as defaults
from Plotting.DataTypes.Data import Data

class Bars(Data):

    def __init__(self, **kwargs):
        Data.__init__(self, **kwargs)
        defaults.kwargs(self, kwargs)

defaults.load(Bars)
