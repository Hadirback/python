import pickle
import json


PICKLE_FILE = 'group.pickle'
JSON_FILE = 'group.json'


def serialize_to_bytes(group):
    if group:
        return pickle.dumps(group)
    else:
        print('Empty dict - my favourite group! Method serialize_to_bytes')
        return None


def serialize_to_json(group):
    if group:
        return json.dumps(group)
    else:
        print('Empty dict - my favourite group! Method serialize_to_json')
        return None


def write_bytes_data(b_data):
    if b_data:
        with open(PICKLE_FILE, 'wb') as f:
            pickle.dump(b_data, f)
    else:
        print('Empty data! Method write_bytes_data')


def write_json_data(j_data):
    if j_data:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(j_data, f)
    else:
        print('Empty data! Method write_json_data')
