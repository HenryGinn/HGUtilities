import numpy as np

import Defaults as defaults
from Plotting.DataTypes.Data import Data
from Plotting.DataTypes.Bar import Bar

class Bars(Data):
     
    """
    This is a subclass of Data used to create bar charts.
    It takes in a bar object, or an iterable of bar objects,
    and key-word arguments thar are relevant only to the entire
    plot. If you wanted every data series to be the same color,
    you would need to specify that for each bar object, but if
    you wanted a log scale, you would specify that at this level.
    If it does not make sense for two distinct data series to
    have different values for a property, then it should be a
    property of this object. For more detail, look at the
    default values for bars and bar objects.

    Bars.defaults shows a list of optional kwargs.

    For further documentation see the following:
    Bar, Data, and Figures classes
    https://github.com/HenryGinn/HGUtils
    https://github.com/HenryGinn/HGUtils/tree/main/Plotting
    """

    def __init__(self, bar_objects, **kwargs):
        Data.__init__(self, **kwargs)
        defaults.kwargs(self, kwargs)
        self.set_bar_objects(bar_objects)

    def set_bar_objects(self, bar_objects):
        if isinstance(bar_objects, Bar):
            self.bar_objects = [bar_objects]
        else:
            self.set_bar_objects_multiple(bar_objects)

    def set_bar_objects_multiple(self, bar_objects):
        if np.all([isinstance(bar_obj, Bar)
                   for bar_obj in bar_objects]):
            self.bar_objects = list(bar_objects)
        else:
            self.bad_data_objects_exception()

    def bad_data_objects_exception(self):
        message = ("When creating a bars object you must pass "
                   "in an instance of bar or an iterable of "
                   "instances of bar")
        raise TypeError(message)

defaults.load(Bars)
