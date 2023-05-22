import os
import sys
package_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(package_path)

import Defaults as defaults

from Plotting.DataTypes.Line import Line as line
from Plotting.DataTypes.Lines import Lines as lines
from Plotting.Figures import create_figures
