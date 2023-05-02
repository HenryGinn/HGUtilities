import traceback
import os

class LoadDefaults():

    def __init__(self):
        self.set_paths()

    def set_paths(self):
        self.set_module_paths()
        self.set_defaults_path()

    def set_module_paths(self):
        stack = traceback.extract_stack()
        self.main_path = stack[3].filename
        self.module_path = stack[-1].filename

    def set_defaults_path(self):
        self.parent_path = os.path.split(self.main_path)[0]
        self.parent_defaults_path = os.path.join(self.parent_path, "Defaults")
        self.ensure_parent_defaults_path_exists()

    def ensure_parent_defaults_path_exists(self):
        if not os.path.exists(self.parent_defaults_path):
            raise Exception("Could not find Defaults folder at:\n"
                            f"{self.parent_defaults_path}")
