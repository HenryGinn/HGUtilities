#from TesterProgram2 import MyClass
#import Defaults as defaults

#help(defaults)

#obj = MyClass(my_parameter="Gav",
              #new_parameter="Moe")

import numpy as np

import Plotting as plotting

x_values = np.arange(0, 2*np.pi, 0.01)
y_values = np.sin(x_values)

line_obj = plotting.line(x_values, y_values)
lines_obj = plotting.lines([line_obj], a=2)
plots_obj = plotting.plots([lines_obj])
plots_obj.plot()

