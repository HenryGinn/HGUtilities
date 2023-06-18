# Importing
import numpy as np
from hgutilities import plotting

# Set independent variable values
x_values = np.arange(0, 10, 0.5)
y_values = np.arange(0, 10, 0.5)
x_mesh, y_mesh = np.meshgrid(x_values, y_values)

# Set dependent variable values
def get_z_mesh_layer(time_value):
    time_mesh = np.ones(x_mesh.shape) * time_value
    z_mesh_layer = (np.sin(x_mesh + time_mesh)
                    + np.sin(y_mesh + time_mesh))
    return z_mesh_layer

time_values = np.arange(0, 2*np.pi, 0.1)
z_meshes = [get_z_mesh_layer(time_value)
            for time_value in time_values]
z_meshes = np.stack(z_meshes)

# Creating animation
surface_obj = plotting.surface(x_mesh, y_mesh, z_meshes)
surface_objects = [surface_obj]
plotting.create_animations(surface_objects)
