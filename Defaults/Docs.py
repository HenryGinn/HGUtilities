import os
import traceback
import inspect
import sys

class Docs():

    def __init__(self):
        self.extract_module()
        self.process_module_directory()

    def extract_module(self):
        file_name = traceback.extract_stack()[-4].filename
        self.module_path = os.path.split(file_name)[0]
        self.module_name = os.path.split(self.module_path)[1]
        self.module = sys.modules[self.module_name]

    def process_module_directory(self):
        for name, obj in inspect.getmembers(self.module):
            if not inspect.ismodule(obj):
                if hasattr(obj, "__module__"):
                    self.filter_non_module_objects(obj)

    def filter_non_module_objects(self, obj):
        object_module = inspect.getmodule(obj)
        common_path = self.get_common_path(object_module)
        if common_path == self.module_path:
            self.set_object_docs(obj)

    def get_common_path(self, object_module):
        object_module_path = object_module.__file__
        common_path = os.path.commonpath((self.module_path, object_module_path))
        return common_path

    def set_object_docs(self, obj):
        doc_path = self.get_doc_path(obj)
        doc_string = self.get_doc_string_from_path(doc_path)
        obj.__doc__ = doc_string

    def get_doc_path(self, obj):
        module = sys.modules[obj.__module__]
        folder_path = self.get_obj_folder_path(obj, module)
        name = obj.__name__
        doc_path = self.get_doc_path_from_path_data(folder_path, name)
        return doc_path

    def get_obj_folder_path(self, obj, module):
        if inspect.isfunction(obj):
            return os.path.splitext(module.__file__)[0]
        else:
            return os.path.split(module.__file__)[0]

    def get_doc_path_from_path_data(self, folder_path, name):
        doc_file_name = os.path.splitext(name)[0]
        doc_file_name = f"{doc_file_name}.txt"
        doc_path = os.path.join(folder_path, "Documentation", doc_file_name)
        return doc_path

    def get_doc_string_from_path(self, doc_path):
        if os.path.exists(doc_path):
            return self.get_doc_string_from_existing_path(doc_path)
        else:
            return self.get_doc_string_from_non_existing_path(doc_path)

    def get_doc_string_from_existing_path(self, doc_path):
        with open(doc_path, "r") as file:
            doc_string = "".join([line for line in file])
        return doc_string

    def get_doc_string_from_non_existing_path(self, doc_path):
        return ("No documentation exists for this object.\n"
                "It was expected to be found at the following location:\n"
                f"{doc_path}\n")

def docs():
    docs_obj = Docs()
