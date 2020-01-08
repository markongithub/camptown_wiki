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
                except Exception: # so many things could go wrong, can't be more specific.
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
        self.bucket = bucket
        self.key = key
        self.s3 = boto3.client('s3')

    def load(self):
        # thanks to https://stackoverflow.com/a/42737249
        # no try/catch because I want to crash if this fails
        obj = self.s3.get_object(Bucket=self.bucket, Key=self.key)
        return json.loads(obj['Body'].read().decode('utf-8'))

    def dump(self, data):
        self.s3.Object(self.bucket, self.key).put(Body=json.dumps(data))
