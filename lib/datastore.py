import json
import os

def load_local(path):
    default = {}
    if os.path.isfile(path):
        data = default
        with open(path, 'r') as f:
            try:
                data = json.load(f)
            except Exception: # so many things could go wrong, can't be more specific.
                pass
        return data
    else:
        return default

def dump_local(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
