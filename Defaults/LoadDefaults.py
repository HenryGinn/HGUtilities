import traceback
import os

class LoadDefaults():

    @classmethod
    def set_parent_path(cls):
        print(cls)
        print("Lol")

    def __init__(self):
        self.set_paths()

    def set_paths(self):
        self.set_module_paths()
        self.set_parent_defaults_path()
        self.set_defaults_path()

    def set_module_paths(self):
        stack = traceback.extract_stack()
        self.main_path = stack[3].filename
        self.module_path = stack[-4].filename

    def set_parent_defaults_path(self):
        self.parent_path = os.path.split(self.main_path)[0]
        self.parent_defaults_path = os.path.join(self.parent_path, "Defaults")
        self.ensure_parent_defaults_path_exists()

    def ensure_parent_defaults_path_exists(self):
        if not os.path.exists(self.parent_defaults_path):
            raise Exception("Could not find Defaults folder at:\n"
                            f"{self.parent_defaults_path}")

    def set_defaults_path(self):
        common_path = os.path.commonpath((self.main_path, self.module_path))
        self.defaults_path = self.parent_defaults_path
        base = self.module_path
        while base != common_path:
            base, folder_name = os.path.split(base)
            self.defaults_path = os.path.join(self.defaults_path, folder_name)
