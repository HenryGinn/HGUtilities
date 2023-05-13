import json

from Utils.Paths import load_json

class ProcessKwargs():

    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.key_words_to_add = []
        self.process_key_words(**kwargs)
        self.add_key_words_to_defaults()

    def process_key_words(self, **kwargs):
        for key_word, value in kwargs.items():
            self.process_key_word(key_word, value)

    def process_key_word(self, key_word, value):
        setattr(self.obj, key_word, value)
        if key_word not in self.obj.defaults:
            self.key_words_to_add.append(key_word)

    def add_key_words_to_defaults(self):
        original_file_contents = load_json(self.obj.defaults_path)
        new_file_contents = self.add_key_words_to_file_contents(original_file_contents)
        self.save_file_contents(original_file_contents, new_file_contents)

    def add_key_words_to_file_contents(self, file_contents):
        new_key_words_dict = {key_word: None
                              for key_word in self.key_words_to_add}
        file_contents.update(new_key_words_dict)
        return file_contents

    def save_file_contents(self, original_file_contents, new_file_contents):
        if len(original_file_contents) != len(new_file_contents):
            with open(self.obj.defaults_path, "w") as file:
                json.dump(new_file_contents, file, indent=2)
