from Plotting.Figures import Figures
from Plotting.Animate import Animate

def create_figures(data_objects, **kwargs):

    """
    This function will take in a list of data objects
    and produce a set of figures showing them.

    This is an interface for the Figures class, and to
    see a list of optional key-word arguments you can
    look at Figures.defaults and Figure.defaults.

    This also returns the Figures object produced if
    the user wants to work with it directly, but this
    is not encouraged, and should only be necessary if
    a feature has not been implemented.
    
    For further documentation see the following:
    Figures and Data classes
    https://github.com/HenryGinn/HGUtils
    https://github.com/HenryGinn/HGUtils/tree/main/Plotting
    """
    
    figures_obj = Figures(data_objects, **kwargs)
    figures_obj.create_figures(**kwargs)
    return figures_obj

def create_animations(data_objects, **kwargs):

    """
    This function will take in a list of data objects
    and produce an animation. These Data objects are just
    like regular Data objects, but the dependent variable
    should instead be an iterable where each element gives
    the values for a single frame.

    This is an interface for the Animate class, and to
    see a list of optional key-word arguments you can
    look at Animate.defaults, Figures.defaults and
    Figure.defaults.

    This also returns the Figures object produced if
    the user wants to work with it directly, but this
    is not encouraged, and should only be necessary if
    a feature has not been implemented.
    
    For further documentation see the following:
    Animate, Figures, and Data classes
    https://github.com/HenryGinn/HGUtils
    https://github.com/HenryGinn/HGUtils/tree/main/Plotting
    """
    
    figures_obj = Animate(data_objects, **kwargs)
    figures_obj.create_animations(**kwargs)
    return figures_obj
