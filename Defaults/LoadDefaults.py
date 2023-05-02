import traceback
import os

from Utils.Paths import make_file

class LoadDefaults():

    @classmethod
    def build_class(cls):
        cls.main_path = traceback.extract_stack()[3].filename
        cls.parent_path = os.path.split(cls.main_path)[0]
        cls.parent_defaults_path = os.path.join(cls.parent_path, "Defaults")

    def __init__(self):
        self.set_paths()

    def set_paths(self):
        self.paths_setup()
        self.set_defaults_path()
        self.process_defaults_path()

    def paths_setup(self):
        self.module_path = traceback.extract_stack()[-3].filename
        self.defaults_path = self.parent_defaults_path
        self.common_path = os.path.commonpath((self.main_path, self.module_path))

    def set_defaults_path(self):
        base = self.module_path
        while base != self.common_path:
            base, folder_name = os.path.split(base)
            self.defaults_path = os.path.join(self.defaults_path, folder_name)

    def process_defaults_path(self):
        self.defaults_path = os.path.splitext(self.defaults_path)[0] + ".txt"
        make_file(self.defaults_path)
