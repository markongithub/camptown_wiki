import json
import os

class LocalDatastore:
    def __init__(self, path):
        self.path = path

    def load(self):
        default = {}
        if os.path.isfile(self.path):
            data = default
            with open(self.path, 'r') as f:
                try:
                    data = json.load(f)
                except Exception: # so many things could go wrong, can't be more specific.
                    pass
            return data
        else:
            return default

    def dump(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f)
