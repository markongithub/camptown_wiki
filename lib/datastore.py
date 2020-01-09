import json
import os

import boto3


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
                except Exception:  # so many things could go wrong, can't be more specific.
                    pass
            return data
        else:
            return default

    def dump(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f)


class NullDatastore:
    def load(self):
        return {}

    def dump(self, data):
        pass


class S3Datastore:
    def __init__(self, bucket, key):
        self.s3_object = boto3.resource('s3').Object(bucket, key)

    def load(self):
        # thanks to https://stackoverflow.com/a/42737249
        # no try/catch because I want to crash if this fails
        return json.loads(self.s3_object.get()['Body'].read().decode('utf-8'))

    def dump(self, data):
        self.s3_object.put(Body=json.dumps(data))
