
import json


def read_json(file_name):
    file_submission_data = open(file_name)
    return json.load(file_submission_data)

def read_file(file_name):
    file = open(file_name, mode = 'r')
    all_of_it = file.read()
    return all_of_it