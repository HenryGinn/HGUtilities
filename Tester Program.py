"""
from TesterProgram2 import MyClass
import Defaults as defaults

obj = MyClass(my_parameter="Gav",
              new_parameter="Moe")

"""

import numpy as np

import Plotting as plotting

def get_line_obj(function, n):
    x_values = np.arange(0, 2*np.pi, 0.01)
    y_values = function(n * x_values)
    line_obj = plotting.line(x_values, y_values)
    return line_obj

def get_surface_obj(n, m):
    x_values = np.arange(0, 2*np.pi, 0.01)
    y_values = np.arange(0, 2*np.pi, 0.01)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)
    z_values = np.sin(n*x_mesh) + np.cos(m*y_mesh)
    surface_obj = plotting.surface(x_mesh, y_mesh, z_values)
    return surface_obj

lines_obj_1 = plotting.lines([get_line_obj(np.sin, 1)])
lines_obj_2 = plotting.lines([get_line_obj(np.cos, 1)])
lines_obj_3 = plotting.lines([get_line_obj(np.sin, 3)])
lines_obj_4 = plotting.lines([get_line_obj(np.cos, 3)])
lines_objects = [lines_obj_1, lines_obj_2, lines_obj_3, lines_obj_4]

#plotting.create_figures(lines_objects)

surface_objects = [get_surface_obj(n, m)
                   for n in range(1, 3)
                   for m in range(1, 4)]

plotting.create_figures(surface_objects)
