import os
import sys
package_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(package_path)

import Defaults as defaults

from Plotting.Line import Line as line
from Plotting.Lines import Lines as lines
from Plotting.Figures import create_figures
#from Figures import create_figures
