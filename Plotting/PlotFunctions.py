from Plotting.Figures import Figures

def create_figures(data_objects, **kwargs):
    figures_obj = Figures(data_objects, **kwargs)
    figures_obj.create_figures()
    return figures_obj

def create_animations(data_objects, **kwargs):
    figures_obj = Figures(data_objects, **kwargs)
    figures_obj.create_animations()
    return figures_obj
