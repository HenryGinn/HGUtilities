import Defaults as defaults

class Data():
     
    """
    This is a general class that gives the data about
    a plot. This class is not dealt with directly, and
    the user should create one of the subclasses
    
    Lines      For creating line and scatter plots
    Bars       For creating bar charts
    Pie        For creating pie charts
    Surface    For plotting 3d surfaces and contour maps
    Colormap   For creating color plots

    Information such as what data to plot, title data,
    axis labels and settings, and anything else relevant
    to the entire plot should be specified at this level.

    Data.defaults shows a list of optional kwargs.

    For further documentation see the following:
    Subclasses (see above) and Figures classes
    https://github.com/HenryGinn/HGUtils
    https://github.com/HenryGinn/HGUtils/tree/main/Plotting
    """

    def __init__(self, **kwargs):
        defaults.kwargs(self, kwargs)

    def get_frame_count(self):
        raise Exception("This data type does not have animation implemented")

defaults.load(Data)
