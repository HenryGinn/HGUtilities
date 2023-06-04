__author__ = "Henry Ginn"
__date__ = "2023/05/13"
__version__ = "1.0"

import os
import sys
package_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(package_path)

from Defaults.LoadDefaults import LoadDefaults as load
from Defaults.ProcessKwargs import ProcessKwargs as kwargs
from Defaults.Inherit import inherit
from Defaults.Docs import docs

docs()
