import pickle
import json
import os


PICKLE_FILE = 'group.pickle'
JSON_FILE = 'group.json'


def deserialize_bytes(b_data):
    if b_data:
        return pickle.loads(b_data)
    else:
        print('Empty data! Method deserialize_bytes')
        return None


def deserialize_json(j_data):
    if j_data:
        return json.loads(j_data)
    else:
        print('Empty data! Method deserialize_json')
        return None


def deserialize_bytes_from_file():
    if os.path.exists(os.path.join(os.getcwd(), PICKLE_FILE)):
        with open(PICKLE_FILE, 'rb') as f:
            return pickle.load(f)
    else:
        print('File is not exists! Method deserialize_bytes_from_file')
        return None


def deserialize_json_from_file():
    if os.path.exists(os.path.join(os.getcwd(), JSON_FILE)):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        print('File is not exists! Method deserialize_json_from_file')
        return None
