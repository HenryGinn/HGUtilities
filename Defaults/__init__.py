"""
A tool used for handling default values of class variables.

The names and default values of the class variables are stored
as json files in a folder called "Default Settings" that is
placed at the base level of the repository. They can be loaded
in, viewed, and modified.
"""

__author__ = "Henry Ginn"
__date__ = "2023/05/13"
__version__ = "1.0"

import os
import sys
package_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(package_path)

from Defaults.LoadDefaults import LoadDefaults as load
from Defaults.ProcessKwargs import ProcessKwargs as kwargs

