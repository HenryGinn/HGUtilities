import traceback
import inspect
import os
import json

from Utils.Paths import make_file
from Utils.Paths import load_json

class LoadDefaults():

    @classmethod
    def build_class(cls):
        cls.main_path = traceback.extract_stack()[3].filename
        cls.parent_path = os.path.split(cls.main_path)[0]
        cls.parent_defaults_path = os.path.join(cls.parent_path, "Default Settings")

    def __init__(self, cls):
        self.cls = cls
        self.set_paths()
        self.set_defaults()

    def set_paths(self):
        self.paths_setup()
        self.set_defaults_path()
        self.process_defaults_path()

    def paths_setup(self):
        self.module_path = traceback.extract_stack()[-4].filename
        self.cls.defaults_path = self.parent_defaults_path
        self.common_path = os.path.commonpath((self.main_path, self.module_path))

    def set_defaults_path(self):
        base = self.module_path
        while base != self.common_path:
            base, folder_name = os.path.split(base)
            self.cls.defaults_path = os.path.join(self.cls.defaults_path, folder_name)

    def process_defaults_path(self):
        self.cls.defaults_path = os.path.splitext(self.cls.defaults_path)[0] + ".txt"
        make_file(self.cls.defaults_path)

    def set_defaults(self):
        self.cls.defaults = load_json(self.cls.defaults_path)
        for parameter_name, parameter_value in self.cls.defaults.items():
            setattr(self.cls, parameter_name, parameter_value)
        
