import numpy as np

import Defaults as defaults
from Plotting.DataTypes.Data import Data

class Colorplot(Data):

    def __init__(self, x_mesh, y_mesh, z_mesh, **kwargs):
        Data.__init__(self, **kwargs)
        defaults.kwargs(self, kwargs)
        self.set_meshes(x_mesh, y_mesh, z_mesh)

    def set_meshes(self, x_mesh, y_mesh, z_mesh):
        self.x_mesh = x_mesh
        self.y_mesh = y_mesh
        self.z_mesh = z_mesh

defaults.load(Colorplot)
