import numpy as np
import scipy as sc

import Defaults as defaults
import Plotting as plotting
"""
x_values = np.arange(0, 3, 1)
y_values = np.arange(0, 3, 1)
x_mesh, y_mesh = np.meshgrid(x_values, y_values)
t_values = np.arange(0, 4, 1)
t_values = np.multiply.outer(t_values, np.ones(x_mesh.shape))
z_values = x_mesh + y_mesh * t_values
surface_obj_1 = plotting.surface(x_mesh, y_mesh, z_values)
surface_obj_2 = plotting.surface(x_mesh, y_mesh, np.sqrt(z_values))
surface_objects = [surface_obj_1, surface_obj_2]
plotting.create_animations(surface_objects, dark=True)
"""

class VibratingPlate():

    def __init__(self, **kwargs):
        defaults.kwargs(self, kwargs)
    
    def get_surface_obj(self, **kwargs):
        defaults.kwargs(self, kwargs)
        self.set_surface_values()
        title = f"Nodes={self.nodes}, Order={self.order}"
        return plotting.surface(self.x_values, self.y_values, self.z_values,
                                axes=False, title=title, cmap=self.cmap)

    def set_surface_values(self):
        self.set_function_inputs()
        self.set_function_values()
        self.set_x_and_y_plot_values()
        self.set_z_values()

    def set_function_inputs(self):
        self.radius = np.linspace(0, self.radius_limit, self.radius_resolution)
        self.theta = np.linspace(-np.pi, np.pi, self.theta_resolution)
        self.time = np.linspace(0, self.time_limit, self.time_resolution,
                                endpoint=False)

    def set_function_values(self):
        radius_values = self.get_radius_values()
        theta_values = self.get_theta_values()
        self.radius_theta_product = np.outer(theta_values, radius_values)
        self.set_temporal_values()

    def get_radius_values(self):
        l_mn = sc.special.jn_zeros(self.order, self.nodes)[-1]
        radius_values = (sc.special.jn(self.order, l_mn * self.radius))
        return radius_values

    def get_theta_values(self):
        theta_negative = self.theta_minus*np.exp(-1j*self.order * self.theta)
        theta_positive = self.theta_plus*np.exp(1j*self.order*self.theta)
        theta_values = theta_negative + theta_positive
        return theta_values

    def set_temporal_values(self):
        self.time_values = np.exp(-1j*2*np.pi*self.time)

    def set_x_and_y_plot_values(self):
        radius_mesh, theta_mesh = np.meshgrid(self.radius, self.theta)
        self.x_values = radius_mesh * np.cos(theta_mesh)
        self.y_values = radius_mesh * np.sin(theta_mesh)

    def set_z_values(self):
        shape_array = np.ones(self.radius_theta_product.shape)
        time_values = np.multiply.outer(self.time_values, shape_array)
        self.z_values = np.real(self.radius_theta_product * time_values)

defaults.load(VibratingPlate)
"""
vibrating_plate_obj = VibratingPlate()
surface_objects = [vibrating_plate_obj.get_surface_obj(nodes=nodes, order=order,
                                                       cmap="spring", radius_resolution=20,
                                                       theta_resolution=20, time_resolution=10)
                   for nodes in range(1, 4) for order in range(5)]
plotting.create_animations(surface_objects, dark=True, dpi=200, maximise=True)
"""

# Importing
import numpy as np
#import hgutils.plotting

def get_lines_obj(n):
    line_obj = get_line_obj(n)
    title = f"Sin({n}x)"
    x_label = "My x axis label"
    y_label = "My y axis label"
    lines_obj = plotting.lines(line_obj, title=title,
                               x_label=x_label, y_label=y_label)
    return lines_obj

def get_line_obj(n):
    y_values = np.sin(n*x_values)
    line_obj = plotting.line(x_values, y_values)
    return line_obj

# Creation of lines objects
x_values = np.arange(0, 2*np.pi, 0.01)
x_coefficients = list(range(1, 13))
lines_objects = [get_lines_obj(n) for n in x_coefficients]

# Creation of figures
plotting.create_figures(lines_objects, subplots=6)
