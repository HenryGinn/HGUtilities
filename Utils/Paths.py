import os
import json

def make_file(file_path):
    if not os.path.exists(file_path):
        folder_path = os.path.split(file_path)[0]
        make_folder(folder_path)
        make_empty_file(file_path)

def make_empty_file(file_path):
    with open(file_path, "w") as file:
        pass

def make_folder(folder_path):
    if not os.path.exists(folder_path):
        parent_folder_path = os.path.split(folder_path)[0]
        make_folder(parent_folder_path)
        os.mkdir(folder_path)

def load_json(path, suppress_errors=False):
    if suppress_errors:
        return load_json_no_errors(path)
    else:
        return do_load_json(path)

def load_json_no_errors(path):
    try:
        return do_load_json(path)
    except:
        return {}

def do_load_json(path):
    with open(path, "r") as file:
        file_contents = json.load(file)
    return file_contents
