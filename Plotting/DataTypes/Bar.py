import Defaults as defaults

class Bar():
 
    """
    Contains information about a single data series
    on a bar chart. Anything that affects the entire
    chart should be specied upon creation of Bars
    objects.

    Bar.defaults shows a list of optional kwargs.

    For further documentation see the following:
    Bars, Data, and Figures classes
    https://github.com/HenryGinn/HGUtils
    https://github.com/HenryGinn/HGUtils/tree/main/Plotting
    """

    def __init__(self, x_values, y_values, **kwargs):
        defaults.kwargs(self, kwargs)
        self.x_values = x_values
        self.y_values = y_values

defaults.load(Bar)
