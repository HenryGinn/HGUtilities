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

lines_obj_1 = plotting.lines([get_line_obj(np.sin, 1)])
lines_obj_2 = plotting.lines([plotting.line(["Blue", "Red", "Green"], [3, 2, 5])], plot_type="pie")
lines_obj_3 = plotting.lines([plotting.line(["Blue", "Red", "Green"], [3, 2, 5])], plot_type="bar")
lines_objects = [lines_obj_1, lines_obj_2, lines_obj_3]

plotting.plot(lines_objects)

