import Defaults as defaults

class Data():

    def __init__(self, **kwargs):
        defaults.kwargs(self, kwargs)

defaults.load(Data)
