from flask import jsonify
import json

### converting the dataset from CLient API into JSON
def deserializer(request_obj):
    return request_obj.json()