import os
import sys
package_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(package_path)

from Defaults.LoadDefaults import LoadDefaults as load
load.build_class()
