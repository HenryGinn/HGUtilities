import numpy as np

import Plotting as plotting

x_values = np.arange(0, 3, 1)
y_values = np.arange(0, 3, 1)
x_mesh, y_mesh = np.meshgrid(x_values, y_values)
t_values = np.arange(0, 4, 1)
t_values = np.multiply.outer(t_values, np.ones(x_mesh.shape))
z_values = x_mesh + y_mesh * t_values
surface_obj_1 = plotting.surface(x_mesh, y_mesh, z_values)
surface_obj_2 = plotting.surface(x_mesh, y_mesh, np.sqrt(z_values))
surface_objects = [surface_obj_1, surface_obj_2]
plotting.create_animations(surface_objects)
