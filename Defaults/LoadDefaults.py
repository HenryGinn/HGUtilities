import traceback
import inspect
import os
import json

from Utils.Paths import make_file
from Utils.Paths import load_json

class LoadDefaults():

    def __init__(self, cls):
        self.cls = cls
        self.set_defaults_path()
        self.set_defaults()

    def set_defaults_path(self):
        module_path = traceback.extract_stack()[-3].filename
        parent_path, module_file_name = os.path.split(module_path)
        defaults_file_name = f"{os.path.splitext(module_file_name)[0]}.txt"
        self.cls.defaults_path = os.path.join(parent_path, "Default Settings", defaults_file_name)

    def set_defaults(self):
        self.cls.defaults = load_json(self.cls.defaults_path, suppress_errors=True)
        for parameter_name, parameter_value in self.cls.defaults.items():
            setattr(self.cls, parameter_name, parameter_value)
        
