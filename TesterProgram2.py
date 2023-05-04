import Defaults as defaults

class MyClass():

    def __init__(self, **kwargs):
        defaults.kwargs(self, **kwargs)

defaults.load(MyClass)
