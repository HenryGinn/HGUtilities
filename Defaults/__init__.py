import os
import sys
package_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(package_path)

import json

from Defaults.LoadDefaults import LoadDefaults as load
load.build_class()

from Defaults.ProcessKwargs import ProcessKwargs as kwargs
